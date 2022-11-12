from datetime import datetime

from apps.app import db


class Memo(db.Model):
    __tablename__ = "memo"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(50), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
