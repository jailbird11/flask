
Can use **jinja templating** for url links e.g **{{ url_for('index') }}**

template inhritance -  **{% extends 'base.html' %}** to inherit code from base.html 

## To style the page-  [Start bootstrap theme](https://startbootstrap.com/themes/clean-blog/)   
* Right click on download and copy link address  
* To add to terminal:
* Mkdir static
* Cd static
* Wget post link
* Ls 
* Unzip -gh-pages.zip

Added css link to base.html file .

Copied html from index on the bootstrap theme and paseted into my file.

## Add page title - passes data to server:
In run.py in render_template included second argument **page_title="Contact".**  
In pages replace heading with **{{ page_title}}**

## Using or loops in html
Add a 2rd argument in render_template **list_of_numbers=[1, 2, 3]**.   
Create a for loop:
{% for number in list_of_numbers %}
    <p>{{ number }} </p>

{% endfor %}

## Read a JSON file
Import Json in py file.
In about route add:  
  with open("flask/data/company.json", "r") as json_data:   
        data = json.load(json_data)  
    return render_template("about.html", page_title="About", company=data)  

in about template add:   
 {{ company[0]["name"] }} 
   
## For loop
Will iterate through all of the data in the json file down to the *endfor*
and include the HTML and variables we've set.  
 **How to do this:**  
1. Place all the about **informaion** in the **json file**.   
2. Wraped the characther info in a **for loop** with **{% for member in company %}** and at the end **{% endfor %}**.   
3. Replace the name with **{{ member.name }}** usiong the json key value.
4. paragraph with **{{ member.description }}**.   
5. Image source with **{{ member.image_source }}**


