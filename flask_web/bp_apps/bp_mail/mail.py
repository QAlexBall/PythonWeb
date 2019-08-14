'''
Mail BluePrint
'''
from flask import Blueprint, request, render_template, session, redirect,\
                  url_for, flash
#  from flask_mail import Message, Mail
from decorators import login_required
BP = Blueprint('mail', __name__, url_prefix='/mail')


#  @celery.task
#  def send_async_email(msg):
    #  '''
    #  Backgroung task to send an email with Falsk-Mail.
    #  '''
    #  with BP.app_context_processor():
        #  mail.send(msg)


@BP.route('/', methods=['GET', 'POST'])
@login_required
def index():
    '''
    mail index
    '''
    if request.method == 'GET':
        return render_template('mail/index.html')
    #  email = request.form['email']
    #  session['email'] = email
    #  msg = Message('Hello from Flask',
                  #  recipients=[request.form['email']])
    #  msg.body = 'This is a test email sent from a background Celery task.'
    #  if request.form['submit'] == 'Send':
        #  send_async_email.delay(msg)
        #  flash('Sending email to {0}'.format(email))
    #  else:
        #  send_async_email.apply_async(args=[msg], countdown=60)
        #  flash('An email will be send to {0} in one minite'.format(email))
    return redirect(url_for('index'))
