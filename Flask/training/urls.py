from dlask import Flash, url_for
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')

# flask will look for templates in the templates folder
def hello(name=None):
    return render_template('hello.html', name=name)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>'
def profile(username): pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='John Doe')
"""
/
/login
/login?next=/
/user/John%20Doe
"""

@app.route('/login', methods=['GET, 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

url_for('static', filename='style.css')