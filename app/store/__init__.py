from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
import uuid
import minio
from ..utils.minio import minio as minio_client
# Note that store is the name for the Blueprint, useful to upload files in the MinIO service.

# Create a Blueprint
store = Blueprint('store', __name__, template_folder='templates')

@store.route('/')
@login_required
def store_page():
    return render_template("newfiles.html")

@store.route('/upload', methods=['POST'])
def upload():
    print("received post data")
    print(request.files)
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    print("test passed")
    try:
        fdata = file.stream.read()
    #file.save(os.path.join("uploads", f"{uuid.uuid4()}_{secure_filename(file.filename)}"))

        file.seek(0)
        minio_client.put_object(bucket_name="storage", object_name=f"{uuid.uuid4()}_{secure_filename(file.filename)}", data=file.stream, length=len(fdata), content_type=file.content_type, metadata={"FILENAME": secure_filename(file.filename)})

    # minio_client.put_object(bucket_name="storage", object_name=f"{uuid.uuid4()}_{secure_filename(file.filename)}", data=file.stream, length=len(fdata), content_type=file.content_type)
        print("saved")
        flash(f"Le fichier {file.filename} a été enregistré correctement.")
        return redirect(url_for('store.store_page'))
    except:
        flash("Une erreur s'est produite", 'error')
        return redirect(url_for('store.store_page'))