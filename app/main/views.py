from flask import render_template, url_for,redirect
from . forms import BlogForm
from . import main




@main.route('/')
def index():
    return render_template('index.html')
@main.route('/logb',methods=['GET','POST'])
def blog():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():
        blog=Blog(title=blog_form.category.data,blog=blog_form.pitch.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('blog.html',blog_form=blog_form)
