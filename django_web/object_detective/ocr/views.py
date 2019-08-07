from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core import serializers
import os
from ocr.models import Image, Record, Favorite
from ocr.forms import ImageForm
from fuzzywuzzy import fuzz, process
from django.core.paginator import Paginator

# baidu ocr
from aip import AipOcr, AipImageClassify
APP_ID = '11312179'
API_KEY = 'DqugFClbpCktqFeKLoFUKl6d'
SECRET_KEY = 'M3Acc4V2vYuZYYEWzlUFbOfiT7sXAREk'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
client1 = AipImageClassify('16152428',
                           'YPrqfltQoyhz94AA7V9GPIem',
                           'X2myicjnkuPra5rbcMWyCz5fbagKpL9a')
@login_required(login_url='login')
def index(request):
    message = {}

    album = Image.objects.filter(user=request.user).order_by('-upload_date')[:15]
    paginator = Paginator(album, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    message['contacts'] = contacts
    # message['album'] = album
    return render(request, 'ocr/index.html', message)

@login_required(login_url='login')
def original_image(request, id):
    message = {}
    image = Image.objects.filter(id=id).first()
    message['image'] = image
    return render(request, 'ocr/original_image.html', message)

@login_required(login_url='login')
def favorite(request):
    message = {} 
    favorites = Favorite.objects.filter(user=request.user).order_by('-add_date')[:15]
    message['favorites'] = favorites
    return render(request, 'ocr/favorite.html', message)

@login_required(login_url='login')
def add_to_favorite(request, id):

    image = Image.objects.filter(id=id).first()
    images = Image.objects.filter(favorite__user=request.user).all()
    if image not in images:
        favorite = Favorite(user=request.user, image=image)
        favorite.save()
    else:
        print('image already in favorite')
    return redirect('favorite')

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

@login_required(login_url='login')
def upload_image(request):
    message = {}
    image_form = ImageForm()
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        img_path = str(request.FILES.get('img_path'))
        if not request.FILES.get('img_path'):
            return HttpResponse('error')
        message['path'] = img_path
        if image_form.is_valid():
            image_form_instance = image_form.save(commit=False)
            image_form_instance.user = request.user
            image_form_instance.tag = '其他'
            image_form_instance.save()
            return redirect('target')
    message['form'] = image_form
    return render(request, 'ocr/upload.html', message)

def target(request):
    tag = []
    image = Image.objects.all().last()
    target_image = get_file_content('ocr/static/media/' + str(image.img_path))
    results = client1.advancedGeneral(target_image)
    print(results)
    for item in results.get('result'):
        if item.get('score') > 0.25:
            tag.append((item.get('keyword'), item.get('root')))
    if len(tag) == 0:
        tag = ['其他']
    Image.objects.filter(id=image.id).update(tag=str(tag))
    return redirect('index')


@login_required(login_url='login')
def image(request, id):
    message = {}
    end = []
    image = Image.objects.filter(id=id).first()
    message['image'] = image
    ocr_image = get_file_content('ocr/static/media/' + str(image.img_path))
    result = client.basicGeneral(ocr_image)
    result = result['words_result']
    for word in result:
        end.append(word.get('words'))
    result = str(end)

    # add to history
    if request.method == 'POST':
        images = Image.objects.filter(record__user=request.user).all()
        result = request.POST.get('result')
        if image not in images:
            new_record = Record(user=request.user, text_image=image, result=result)
            new_record.save()
        else:
            Record.objects.filter(text_image=image).update(result=result)
        return redirect('history')

    message['result'] = result
    return render(request, 'ocr/image.html', message)

@login_required(login_url='login')
def history(request):
    message = {}
    records = Record.objects.filter(user=request.user).order_by('-record_date')[:15]
    message['records'] = records
    return render(request, 'ocr/history.html', message)

def search(request):
    message = {}
    search_result = []

    if request.method == 'POST':
        images = Image.objects.all()
        for image in images:
            distance = fuzz.token_set_ratio(image.tag, request.POST.get('keyword'))
            if distance > 0:
                search_result.append((image, distance))
        search_result = sorted(search_result, key=lambda x : x[1])
        message['search_result'] = search_result[::-1]
        print(search_result)
        return render(request, 'ocr/search.html', message)

    return render(request, 'ocr/search.html', message)

@login_required(login_url='login')
def delete_image(request, id):
    message = {}
    image = Image.objects.filter(id=id).first()
    
    if request.method == 'POST':
        confirm_info = request.POST['confirm']
        if confirm_info == 'y':
            img_path = str(os.getcwd() + '/ocr/static/media/' + str(image.img_path))
            os.remove(img_path)
            image.delete()
            return redirect('index')
        else:
            return redirect('index')

    message['image'] = image
    return render(request, 'ocr/delete.html', message)

@login_required(login_url='login')
def image_enhancement(request, id):
    pass


def register(request):
    message = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not email or not password1 or not password2:
            message['error_info'] = '请输入完整的注册信息'
        else:
            if User.objects.filter(username=username) or User.objects.filter(email=email):
                message['user_exist'] = '用户名或邮箱已经存在!'
            elif password1 != password2:
                message['password_not_same'] = '两次密码不同!'
            else:
                user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password1)
                user.save()
                user_login = authenticate(request, username=username, email=email, password=password1)
                login(request, user_login)
                return redirect('index')

    return render(request, 'ocr/register.html', message)

def user_login(request):
    message = {}

    if request.method == 'POST':
        if not request.POST.get('username'):
            message['no_username'] = '用户名为空'
        elif not request.POST.get('password'):
            message['no_password'] = '密码为空'
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message['error'] = '用户名或密码错误'

    return render(request, 'ocr/login.html', message)

def user_logout(request):
    logout(request)
    return redirect('index')