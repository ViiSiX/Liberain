"""This module include console commands for Liberain."""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ..liberain import app, db
from ..models import models


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
