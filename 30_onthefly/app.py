# The Tallyers: Saxon, Rona, and Marcos
# Software Development
# K30 -- Who Do Forms Work For?
# 10/19/2026


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

app = Flask(__name__)

@app.route("/")
def mimic():
    return render_template('index.html')

if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()