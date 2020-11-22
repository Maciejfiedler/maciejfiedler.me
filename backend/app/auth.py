from flask import redirect, request, url_for, render_template, flash
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
        return render_template('login.html')

    email = request.form['email']
    if email in users:
        if request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return redirect(url_for('admin.index'))
        else:
            flash("The password is incorrect.", 'error')
            return redirect(url_for('login'))
    else:
        flash("The email or password is incorrect.", 'error')
        return redirect(url_for('login'))

    flash("Something went wrong.", 'error')
    return redirect(url_for('login'))

# @app.route('/logout')


def logout():
    flask_login.logout_user()
    return render_template('message.html', message="You logged out. See you next time 👋️")
