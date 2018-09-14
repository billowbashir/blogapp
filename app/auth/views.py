from flask import render_template,redirect,url_for
from . import auth
from .forms import LoginForm,RegistrationForm


@auth.route('/register')
def register():
    reg_form=RegistrationForm()
    return render_template('auth/registration.html',reg_form=reg_form)


@auth.route('/login')
def login():
    login_form=LoginForm()
    return render_template('auth/login.html',login_form=login_form)
