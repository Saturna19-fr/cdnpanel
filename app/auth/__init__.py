from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from ..utils.user import User, fetch_user
from flask_login import login_user, logout_user
# Create a Blueprint
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        code = request.form.get('code')



        user = fetch_user(username)

        if not user:
            return redirect(url_for("auth.login"))
        
        if user.password == code:
            login_user(user)
            flash("Login successful.")
            return redirect(url_for("views.home"))
        else:
            flash("Login incorrect.")
            return redirect(url_for("auth.login"))
    return render_template('login.html')

@auth.route("/logout", methods=['GET', "POST"])
def logout():
    logout_user()
    return redirect(url_for("views.home"))