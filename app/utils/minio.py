from dotenv import load_dotenv 
from minio import Minio
import os

load_dotenv()

minio = Minio(
        endpoint="cdn-minio.vofasn.easypanel.host/",
        access_key=os.environ["MINIO_ACCESS_KEY"],
        secret_key=os.environ["MINIO_SECRET_KEY"],
        secure=True
    )

# minio.fput_object(bucket_name="storage", object_name="test.new.txt", file_path="test.txt", content_type="text/plain")

