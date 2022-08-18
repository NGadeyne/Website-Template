from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
    
    