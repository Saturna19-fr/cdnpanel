from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, name, password, id):
        self.id = id
        self.password = password
        self.name = name


def fetch_user(username) -> User:
    return next((u for u in users_dict_updated.values() if u.name == username), None)

users_dict_updated = {
    "1": User(name="saturna", password="1234", id="1")
}

# users_dict = {"saturna": User(password="1234", id=1), "pablo": User(password="5678", id=2)}