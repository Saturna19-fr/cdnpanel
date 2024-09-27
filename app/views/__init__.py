from flask import Blueprint, render_template, request, redirect, url_for, flash

# Create a Blueprint
views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def home():
    return render_template("homepage.html")

@views.route('/about')
def about():
    return "about page"

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # You can add logic to handle the form data here
        
        flash('Message sent successfully!', 'success')
        return redirect(url_for('views.contact'))
    
    return "contact page"