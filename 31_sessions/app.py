# The Tallyers: Saxon, Rona, and Marcos
# Software Development
# K31 -- Take and Keep
# 10/20/2026


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import session
from flask import request
from flask import url_for
from flask import redirect
import csv

app = Flask(__name__)
app.secret_key = b"tallyers"


with open ("data/users.csv", 'r') as file:
    reader = csv.DictReader(file)
    accounts = {x['Username']:x['Password'] for x in reader}


@app.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('response'))
    else:
        return redirect(url_for('login'))


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username')
    return render_template('logout.html')

@app.route("/auth/login")
def response():
    if 'username' in session:
        return render_template('response.html', username=session['username'], error_message_login = "")
    
    name = request.args['username']
    password = request.args['password']
    
    # check on username and password fields. either login or reload
    # depending on what they are.
    if name == "" or password == "":
        # if empty password or empty name field
        return render_template('login.html', error_message_login = "Fill out all credentials")

    if name in accounts.keys():
        if accounts[name] == password:
            # if the login credentials are correct
            session['username'] = name
            return render_template('response.html', username=name, error_message_login = "") 
        else:
            # if the login credentials are wrong
            return render_template('login.html', error_message_login = "Incorrect password")

    else:
        return render_template('login.html', error_message_login = "No account under this username")
    
@app.route("/auth/register")
def response_register():
    name = request.args['new_username']
    password = request.args['new_password']
    if name == "" or password == "":
        return render_template('login.html', error_message_register = "Fill out all credentials")
    with open ("data/users.csv", 'a') as file:
        if name in accounts.keys():
            return render_template('login.html', error_message_register = "Username taken")
        writer = csv.writer(file)
        writer.writerow([name, password])
        accounts[name] = password
    return render_template('response.html', username=request.args['new_username'], error_message_login = "") 
        



if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()