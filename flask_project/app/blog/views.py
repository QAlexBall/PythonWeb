''' blog views '''
from flask import render_template
from flask_login import login_required
from . import blog

content = """
# README
## README
### README
"""

@login_required
@blog.route('/')
def index():
    ''' blog index '''
    return render_template('blog/index.html', text=content)


@login_required
@blog.route('/edit/', methods=['GET', 'POST'])
def edit():
    ''' write blog '''
    return render_template('blog/md.html')
