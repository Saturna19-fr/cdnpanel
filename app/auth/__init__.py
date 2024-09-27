from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# Create a Blueprint
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = request.form.get('code')
        # Add your authentication logic here
        if code == "6336":
            session["logged_in"] = True
            flash('Login successful!', 'success')
            return redirect(url_for('views.about'))
        else:
            flash("Vous n'êtes pas ma sublime personne.", 'danger')
    return render_template('login.html')