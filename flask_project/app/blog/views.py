''' blog views '''
from flask import render_template
from . import blog

content = """
# README
## README
### README
"""


@blog.route('/')
def index():
    ''' blog index '''
    return render_template('blog/index.html', text=content)


@blog.route('/edit/<int:id>/', methods=['GET', 'POST'])
def write():
    ''' write blog '''
    
    return render_template('blog/md.html')
