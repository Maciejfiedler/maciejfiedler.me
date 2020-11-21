from flask import redirect, request, url_for
import flask_login
import json

with open('users.json') as myfile:
    jsonfile = myfile.read()

loadedjson = json.loads(jsonfile)
users = loadedjson['users']


class User(flask_login.UserMixin):

    @property
    def is_authenticated(self):
        return True


# @login_manager.user_loader
def user_loader(email):
    if email not in users:
        return "Can't find your email here :("

    user = User()
    user.id = email
    return user


# @login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


# @app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <label for="fname">Email</label><br>
                <input type='text' name='email' id='email'/><br>
                <label for="fname">Password</label><br>
                <input type='password' name='password' id='password'/><br>
                <input type="submit" value="Submit">
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect('admin')

    return 'Bad login'

# @app.route('/logout')


def logout():
    flask_login.logout_user()
    return 'Logged out'
