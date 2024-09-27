from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
# Note that store is the name for the Blueprint, useful to upload files in the MinIO service.

# Create a Blueprint
store = Blueprint('store', __name__, template_folder='templates')

@store.route('/')
def store_page():
    return render_template("newfiles.html")

@store.route('/upload', methods=['POST'])
def upload():
    print("received post data")
    print(request.files)
    if 'file' not in request.files:
        print("no file")
        flash('No file part')
        return redirect(request)
    file = request.files['file']
    if file.filename == '':
        print("no file name")
        flash('No selected file')
        return redirect(request)
    file.save(secure_filename(file.filename))
    print("saved")
    return redirect(url_for('store.store_page'))