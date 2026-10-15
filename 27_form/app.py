# The Plads: Saxon, Sara, and Richard
# Software Development
# K27 -- Who Do Forms Work For?
# 10/14/2026

# CONVENTIONS FOR IMPORTS:
# list most general first (ie standard python library, no pip install req'd)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (eg today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0                     #"home-rolled" module for basic exploration

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will NOT.

TASK: Predict which .
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''


#USAGE: Uncomment one version of the decorator at a time

@app.route("/") 
#@app.route( "/", methods=['GET'] )
#@app.route( "/", methods=['POST'] ) # cannot make GET requests, so nothing works
#@app.route( "/", methods=['GET', 'POST'] ) # allows both types of requests
def disp_loginpage(): # all referenced printing is in the terminal
    #print("\n\n\n") # it just adds 3 empty lines...
    #print("***DIAG: this Flask obj ***") # prints out verbatim string
    #print(app) # prints <Flask 'app'> in terminal
    #print("***DIAG: request obj ***") # prints string verbatim. same as before
    #print(request) # prints out the requested website and the type of request (GET)
    #print("***DIAG: request.args ***") # just prints the string
    #print(request.args) # prints out the type of data structure used: ImmutableMultiDict([])
    #print("***DIAG: request.args['username']  ***") # probably the verbatim string
    #print(request.args['username']) # doesn't work
    #print("***DIAG: request.headers ***") # string
    #print(request.headers) # prints out website and web browser data
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # YOUR CODE HERE
    # ...for experimenting with
    # home-rolled module importation
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #print(testmod0.goo()) # prints the string that goo returns in the terminal
    return render_template( 'login.html' )



#USAGE: Uncomment one version of the decorator at a time

#@app.route("/auth")
#@app.route( "/auth", methods=['GET'] )
@app.route( "/auth", methods=['POST'] )
#@app.route( "/auth", methods=['GET', 'POST'] )
def authenticate(): # things only printed (still in the terminal) when a username is input and submitted. otherwise the same as disp_loginpage().
    #print("\n\n\n") # prints 3 lines
    #print("***DIAG: this Flask obj ***")
    #print(app) #prints <Flask 'app'> in terminal
    #print("***DIAG: request obj ***")
    #print(request) # prints <Request 'link' [GET]>
    #print("***DIAG: request.args ***")
    #print(request.args) # prints parameters
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) # this prints out the username when you submit it
    #print("***DIAG: request.headers ***")
    #print(request.headers) #metadata
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # YOUR CODE HERE
    # ...for experimenting with
    # home-rolled module importation
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    username = request.args['username']
    return  username # "Waaaa hooo HAAAH" response to a form submission

    
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