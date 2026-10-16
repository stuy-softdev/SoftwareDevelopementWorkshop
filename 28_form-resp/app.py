# Saxon Rassner, Rona Wassercug, Marcos Lehman
# Software Development
# K28 -- Take and Give
# 2026-10-15r
# time spent: 0.4 + (...)

# CONVENTIONS FOR IMPORTS:
# list most general first (ie standard python library, no pip install req'd)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (eg today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") 
#@app.route( "/", methods=['GET'] )
#@app.route( "/", methods=['POST'] )
#@app.route( "/", methods=['GET', 'POST'] )
def disp_loginpage():
    return render_template( 'login.html')



#USAGE: Uncomment one version of the decorator at a time

@app.route("/auth")
#@app.route( "/auth", methods=['GET'] )
#@app.route( "/auth", methods=['POST'] )
#@app.route( "/auth", methods=['GET', 'POST'] )
def authenticate():
    return render_template( 'response.html', username=request.args['username'])  #response to a form submission


if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()


'''
~~~
    the BEEG REWARD
        ...for reading all the way to "The Waybottom."
                                                       ~~~

The Question du Jour is

How do GET & POST requests 
relate to 
request.args and request.headers?

...and the best way to engage with this Q 
is to selectively uncomment targeted regions above,
making a prediction before each successive re-run/re-load, 
and making sense of observations.

(after you have made some sense of things, document this in readme)

'''