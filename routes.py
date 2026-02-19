import os
import uuid
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename

from extensions import db
from models import Image
from process_choice import user_choice

upload_bp = Blueprint("upload", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "no image file provided"}), 400

    file = request.files["image"]
    operation = request.form.get("process")

    if file.filename == "":
        return jsonify({"error": "no selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "file type not supported"}), 400

    original_filename = secure_filename(file.filename)

    image_uuid = str(uuid.uuid4())

    ext = original_filename.rsplit(".", 1)[1].lower()
    new_filename = f"{image_uuid}.{ext}"

    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)

    filepath = os.path.join(upload_folder, new_filename)

    file.save(filepath)

    file_size = os.path.getsize(filepath)

    img = Image(
        filename=new_filename,
        path=filepath,
        size=file_size
    )

    db.session.add(img)
    db.session.commit()

    output_image = user_choice(choice = operation, image=filepath)


    return jsonify({
        "message": " uploaded ",
        "id": img.id,
        "filename": img.filename,
        "path": img.path,
        "size": img.size,
        "output": output_image
    }), 201 
