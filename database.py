''' File to hold empty DB object to avoid circular import issues '''
from flask_sqlalchemy import SQLAlchemy
DB = SQLAlchemy()
