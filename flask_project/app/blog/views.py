''' blog views '''
from flask import render_template
from flask_login import login_required
from . import blog

content = """
# README
## README
### README
"""

@blog.route('/')
@login_required
def index():
    ''' blog index '''
    return render_template('blog/index.html', text=content)


@blog.route('/edit/', methods=['GET', 'POST'])
@login_required
def edit():
    ''' write blog '''
    return render_template('blog/md.html')
