# app/main.py

from flask import Flask, render_template, request
import pandas as pd
from app.contact import ContactForm

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'

    @app.route('/')
    def homepage():
        return render_template('views/homepage.html')
    
    @app.route('/about')
    def about():
        return render_template('views/about.html')
    
    @app.route('/contact', methods=["GET", "POST"])
    def get_contact():
        form = ContactForm(request.form)
        if request.method == 'POST':
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            message = request.form["message"]
            res = pd.DataFrame({'name': name, 'email': email, 'subject': subject, 'message': message}, index=[0])
            res.to_csv('./contactusMessage.csv')
            return render_template('views/contact.html', form=form)
        else:
            return render_template('views/contact.html', form=form)

    return app