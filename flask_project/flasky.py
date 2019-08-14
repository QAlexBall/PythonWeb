import os
from app import create_app,db
from flask_script import Manager
#  from app.models import User, Role
from flask_migrate import Migrate, upgrade

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

#  @app.shell_context_processor
#  def make_shell_context():
    #  return dict(db=db, User=User, Role=Role)

if __name__ == "__main__":
    manager.run()
