from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField




class ContactForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = EmailField("Your Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()], render_kw={'class': 'form-control', 'rows': 5})
    submit = SubmitField("Send")



