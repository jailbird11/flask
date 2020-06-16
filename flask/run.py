# imports flask
import os
from flask import Flask, render_template 

# Creates an instances of this and stores in an variable called app
app = Flask(__name__) 

# app route decorator-starts with @. Links to pages
@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3]) 

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
# Only use debug for testing not for project