from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "iugeu_zhui(-è_hfroe'fhrijehè)"


    # print(minio.list_buckets())
    # print(f"https://cdn-minio.vofasn.easypanel.host/storage/test.txt")

    # # minio.fput_object("storage", "test.txt", "test.txt")
    # a = minio.fget_object("storage", "test.txt", "test.txt")
    # a.
    from .views import views
    from .auth import auth
    from .buckets import buckets
    from .store import store

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(buckets, url_prefix='/buckets/')
    app.register_blueprint(store, url_prefix='/store/')


    return app