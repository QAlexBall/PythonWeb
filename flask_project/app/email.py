""" email """
from flask import Blueprint, render_template, request, flash, \
    url_for, session, redirect
email_bp = Blueprint('email', __name__, url_prefix='/email')
from .tasks import send_async_email


@email_bp.route('/', methods=['GET', 'POST'])
def index():
    ''' email index '''
    if request.method == 'GET':
        return render_template('mail/index.html')

    email = request.form['email']
    session['email'] = email
    # send the email
    email_data = {
        'subject': 'Hello from Flask',
        'to': email,
        'body': 'This is a test email sent from a background Celery task.'
    }
    if request.form['submit'] == 'Send':
        # send right away
        res = send_async_email.delay(email_data)
        print(res.get())
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[email_data], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))
    return redirect(url_for('email.index'))
