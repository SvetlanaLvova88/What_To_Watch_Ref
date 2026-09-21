from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('settings.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import models  # noqa: E402, F401
from . import forms  # noqa: E402, F401
from . import views  # noqa: E402, F401
from . import error_handlers  # noqa: E402, F401
from . import cli_commands  # noqa: E402, F401
