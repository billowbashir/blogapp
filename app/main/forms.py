from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import Blog,Comment

class BlogForm(FlaskForm):
    title=SelectField('title',
        choices=[('sports', 'sports'), ('life style', 'life style'), ('tech', 'tech'), ('funny', 'funny')], validators = [Required()])
    blog = TextAreaField('pitblogch',validators=[Required()])
    submit = SubmitField('submit')
# class CommentForm(FlaskForm):
#     comment=TextAreaField('comment',validators=[Required()])
#     submit = SubmitField('submit')
