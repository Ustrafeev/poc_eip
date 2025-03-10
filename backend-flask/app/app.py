from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_uploads import configure_uploads, IMAGES, UploadSet
from werkzeug.utils import secure_filename
import io
import os
from image_models import Image  # Import your Image model
from extensions import db  # Import the db object

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Requests if needed

# For PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mike:mike@localhost/dbnest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'  # Set a default upload folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# Flask-Uploads configuration
app.config['UPLOADER_DEST'] = os.path.join(app.root_path, 'uploads')  # Set destination folder for uploads

db.init_app(app)  # Initialize db with app (instead of passing app directly)

# Flask-Uploads setup
# Flask-Uploads setup
photos = UploadSet('photos', IMAGES)

# Configure Flask-Uploads with a destination folder
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(), 'uploads')

# Apply the configuration to the upload set
configure_uploads(app, photos)


# Create tables
with app.app_context():
    db.create_all()

@app.route('/image/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        mimetype = file.mimetype
        data = file.read()  # Read the file content as binary data
        new_image = Image(filename=filename, mimetype=mimetype, data=data)
        db.session.add(new_image)
        db.session.commit()
        return jsonify({'message': 'File uploaded successfully', 'id': new_image.id}), 201

@app.route('/image/<int:id>', methods=['GET'])
def get_image(id):
    image = Image.query.get(id)
    if image is None:
        return jsonify({'message': 'Image not found'}), 404
    return send_file(
        io.BytesIO(image.data),
        mimetype=image.mimetype,
        as_attachment=True,
        download_name=image.filename
    )

@app.route('/')
def index():
    return 'Welcome to Digital Wardrobe API!'

if __name__ == '__main__':
    app.run(debug=True)
