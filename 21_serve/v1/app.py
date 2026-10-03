# Saxon Rassner
# Team Name
# Software Development
# 10/3/2026
# K21 -- Would You Like Fries With That?

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

