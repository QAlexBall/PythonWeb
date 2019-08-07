from django.contrib import admin
from ocr.models import Image, Record, Favorite
from django.utils.html import format_html
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    
    def show_image(self, obj):
        url = '/static/media/' + str(obj.img_path)
        return format_html('<img src="{}" width="100" height="80" />'.format(
            url))

    list_display = ('id', 'show_image', 'upload_date', 'tag')


admin.site.register(Image, ImageAdmin)

class RecordAdmin(admin.ModelAdmin):

    def show_image(self, obj):
        url = '/static/media/' + str(obj.text_image.img_path)
        return format_html('<img src="{}" width="100" height="80" />'.format(url))

    list_display = ('user', 'show_image', 'record_date', 'result')

admin.site.register(Record, RecordAdmin)

class FavoriteAdmin(admin.ModelAdmin):

    def show_image(self, obj):
        url = '/static/media/' + str(obj.image.img_path)
        return format_html('<img src="{}" width="100" height="80" />'.format(url))

    list_display = ('user', 'show_image', 'add_date')
admin.site.register(Favorite, FavoriteAdmin)