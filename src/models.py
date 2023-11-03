from sqlalchemy import Integer
from datetime import datetime
from . import db

class Projects(db.Model):
    id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
    Title = db.Column(db.String(128), nullable=False,)
    Description = db.Column(db.String(512), nullable=True,)
    Completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)

    def toDict(self):
        return {
            'id': self.id,
            'Title': self.Title,
            'Description': self.Description,
            'Completed': self.Completed,
            'created_at': self.created_at.isoformat()  # Format the datetime as ISO 8601
        }
