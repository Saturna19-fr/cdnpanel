from flask import Flask
from flask_login import LoginManager

from .utils.user import users_dict_updated
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "iugeu_zhui(-è_hfroe'fhrijehè)"

    from .views import views
    from .auth import auth
    from .buckets import buckets
    from .store import store

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(buckets, url_prefix='/buckets/')
    app.register_blueprint(store, url_prefix='/store/')
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    @login_manager.user_loader
    def load_user(user_id):
        user_data = users_dict_updated.get(user_id)
        return user_data


    login_manager.init_app(app)
    return app