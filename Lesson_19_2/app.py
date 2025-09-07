from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory, url_for
from werkzeug.utils import secure_filename
import mimetypes
import os

app = Flask(__name__)

# Налаштування збереження
UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


def is_image(file_storage) -> bool:
    mt = file_storage.mimetype or mimetypes.guess_type(file_storage.filename)[0]
    return bool(mt) and mt.startswith("image/")


# Маршрути

@app.route("/")
def root():
    return (
        "Server is up.<br>"
        "POST /upload (form-data key=image)<br>"
        "GET /image/&lt;filename&gt; -> JSON with URL<br>"
        "GET /uploads/&lt;filename&gt; -> file<br>"
        "DELETE /delete/&lt;filename&gt;<br>"
    )


# Віддати файл напряму
@app.route("/uploads/<path:filename>")
def serve_upload(filename):
    return send_from_directory(UPLOAD_DIR, filename)


# Завантаження зображення
@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "Field 'image' is required"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not is_image(file):
        return jsonify({"error": "Only images are allowed"}), 400

    filename = secure_filename(file.filename)
    file.save(UPLOAD_DIR / filename)

    image_url = url_for("serve_upload", filename=filename, _external=True)
    return jsonify({"image_url": image_url}), 201


# Завжди повертаємо JSON з URL
@app.route("/image/<path:filename>", methods=["GET"])
def get_image_url(filename):
    filepath = UPLOAD_DIR / filename
    if not filepath.exists():
        return jsonify({"error": "Image not found"}), 404
    image_url = url_for("serve_upload", filename=filename, _external=True)
    return jsonify({"image_url": image_url}), 200


# Видалення зображення
@app.route("/delete/<path:filename>", methods=["DELETE"])
def delete_image(filename):
    filepath = UPLOAD_DIR / filename
    if not filepath.exists():
        return jsonify({"error": "Image not found"}), 404
    os.remove(filepath)
    return jsonify({"message": f"Image {filename} deleted"}), 200


# Запуск СЕРВЕРА (має бути останнім)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

