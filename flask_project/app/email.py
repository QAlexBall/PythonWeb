""" email """
from flask import Blueprint, render_template, request, flash, \
    url_for, session, redirect, jsonify
from flask_login import login_required
email_bp = Blueprint('email', __name__, url_prefix='/email')
from .tasks import send_async_email, long_task


@login_required
@email_bp.route('/', methods=['GET', 'POST'])
def index():
    ''' email index '''
    if request.method == 'GET':
        return render_template('mail/index.html')
    email = request.form['email']
    session['email'] = email
    email_data = {
        'subject': 'Hello from Flask',
        'to': email,
        'body': 'This is a test email sent from a background Celery task.'
    }
    if request.form['submit'] == 'Send':
        send_async_email.delay(email_data)
        flash('Sending email to {0}'.format(email))
    else:
        send_async_email.apply_async(args=[email_data], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))
    return redirect(url_for('email.index'))


@login_required
@email_bp.route('/longtask/', methods=['POST'])
def longtask():
    ''' try long task '''
    task = long_task.apply_async()
    return jsonify({}), 202, {
        'Location': url_for('taskstaus', task_id=task.id)
    }


@login_required
@email_bp.route('/status/<task_id>')
def task_status(task_id):
    ''' task status '''
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),
        }
    return jsonify(response)
