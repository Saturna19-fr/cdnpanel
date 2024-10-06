from flask import Blueprint, render_template, request, redirect, url_for, flash
from minio import Minio
from ..utils.minio import minio
from ..utils.filetypes import get_file_type
from ..utils.obj import CDNO

# Create a Blueprint
buckets = Blueprint('buckets', __name__, template_folder='templates')

@buckets.route('/')
def home():
    return f"404: Bucket non fourni."

@buckets.route('/<string:bucket_name>')
def search_by_bucket(bucket_name:str):
    try:
        if not minio.bucket_exists(bucket_name):
            return f"404 Bucket non existant"
        a = minio.list_objects(bucket_name)
        do = []
        for minobj in a:
            obj2 = minio.stat_object(bucket_name=bucket_name, object_name=minobj.object_name)

            obj = CDNO(minobj.object_name, bucket_name, special_name = obj2.metadata.get("X-Amz-Meta-Filename"))
            do.append(obj)
        return render_template("bucketlist.html", bucket_name=bucket_name, objects=do)
    except:
        flash("Une erreur de conenction a MinIO s'est produite", "error")
        return redirect(url_for("app.home"))