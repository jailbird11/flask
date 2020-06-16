
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