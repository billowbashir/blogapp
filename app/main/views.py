from flask import render_template, url_for,redirect
from . forms import BlogForm
from ..models import Blog
from . import main
from .. import db




@main.route('/')
def index():
    blogs=Blog.query.all()
    return render_template('index.html', blogs=blogs)
@main.route('/logb',methods=['GET','POST'])
def blog():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():
        blog=Blog(title=blog_form.title.data,blog=blog_form.blog.data,user_id=current_user.id.username)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('blog.html',blog_form=blog_form)
