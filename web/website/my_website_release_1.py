"""
Python for web development

We have many frameworks for web development
- bottle framework
- flask framework # Popular and it is MICRO Framework
- django framework # Popular and it is MVT Framework MVT-Model View Template
- web2py framework
- pyramid framework
- falcon framework
- fastapi framework # Getting Popularity
Many More
"""

"""
Using flask framework
1) we can develop website
2) we can develop RESTFul web services like REST-API, Micro services
"""

"""
For any web application we need 3 things
1) web server: flask has builtin server - This can be used for development purpose ONLY
    List Of Production Servers:
    https://wsgi.readthedocs.io/en/latest/servers.html
2) database: SQLite
3) browser
"""

"""
In this section, we will discuss
How to use flask for website development 
"""


# ------------
# Create app for our website
##############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__) # __name__ = '__main__'
####################################

# EMPTY WEBSITE. WE HAVE NOT CREATED ANY PAGES

# ------------
# Run builtin server
##############
my_website_app.run(debug=True)
# my_website_app.run(debug=True, host='', port='')
####################################