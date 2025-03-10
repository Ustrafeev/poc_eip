# image_models.py
from extensions import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    mimetype = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, filename, mimetype, data):
        self.filename = filename
        self.mimetype = mimetype
        self.data = data
