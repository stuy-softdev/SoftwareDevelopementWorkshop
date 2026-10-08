# Clyde 'Thluffy' Sinclair
# Software Development
# Sep 2026

# DEMO
# basics of /static folder
from flask import Flask
app = Flask(__name__)

@app.route("/")             # bind the root route to this function. Ie serve this function's return value when the root route is requested.
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    
    # UNCOMMENT NEXT LINE TO SEE PSOD
    # a = 1/0
    
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported 
    app.debug = True        # enable auto-restart of web server upon code change
    app.run()

'''
we predict that the console will have:
    the __name__ of this module is... \n__main__
and the site will say
    No hablo queso!
    
result: this did happen.
'''