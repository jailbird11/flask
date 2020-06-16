# imports flask
import os
import json
from flask import Flask, render_template 

# Creates an instances of this and stores in an variable called app
app = Flask(__name__) 

# app route decorator-starts with @. Links to pages
@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    with open("flask/data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) 

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 

