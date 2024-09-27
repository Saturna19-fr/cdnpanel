from minio import Minio

minio = Minio(
        endpoint="cdn-minio.vofasn.easypanel.host/",
        access_key="o0LvzjtyIUCj36sNVETb",
        secret_key="J4lHYpH6y30w78RXj8ZFTfQCG10cJYHoMaS31UMt",
        secure=True
    )

minio.fput_object(bucket_name="storage", object_name="test.new.txt", file_path="test.txt", content_type="text/plain")

