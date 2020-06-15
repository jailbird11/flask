# imports flask
import os
from flask import Flask 

# Creates an instances of this and stores in an variable called app
app = Flask(__name__) 

# app route decorator-starts with @
@app.route("/") 
def indx():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) #Only use debug for testing not for project