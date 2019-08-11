from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import APP
from extensions import db
from models import User

manager = Manager(APP)

# bind app and db
migrate = Migrate(APP, db=db)

# add migrate command to manager
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
