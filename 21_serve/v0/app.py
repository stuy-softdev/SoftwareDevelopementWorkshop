# Saxon Rassner
# Team Name
# Software Development
# 10/3/2026
# K21 -- Would You Like Fries With That?

'''
ERRORS:
<If running this code yielded errors, reproduce them verbatim here.
 ....and if you care to, speculate as to reasons and/or solutions.>
 - ModuleNotFoundError: No module named 'flask'
 - * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
'''


from flask import Flask

app = Flask(__name__)         # Q0: Where have you seen similar syntax in other langs?

@app.route("/")               # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)           # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()                     # Q5: Where have you seen similar constructs in other languages?
