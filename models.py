from datetime import datetime
from extensions import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)   
    path = db.Column(db.String(500), nullable=False)       
    size = db.Column(db.Integer, nullable=False)           
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Image {self.filename} ({self.uuid})>"
