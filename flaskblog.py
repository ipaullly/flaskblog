from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginFrom
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hf76rds'

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
        flash(f'Account created for {(form.username.data)}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginFrom()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)