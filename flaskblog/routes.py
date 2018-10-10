from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationFrom, LoginFrom
from flaskblog.models import User
posts = [
    {
        'author': 'John doe',
        'title': 'blog post dres',
        'content': 'Second post content',
        'date_posted': 'April 32, 2018'
    },
    {
        'author': 'Gory Eshlat',
        'title': 'blog post fux',
        'content': 'the third reich post content',
        'date_posted': 'June 12, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        if form.email.data == 'jotun@gmail.com' and form.password.data == 'password':
            flash(f'You Have Successfully Logged In', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. check login details and try again', 'danger')
    return render_template('login.html', title='Login', form=form)
