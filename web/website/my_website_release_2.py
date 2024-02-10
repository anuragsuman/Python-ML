"""
added welcome page
"""

# ------------
# Create app for our website
##############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__) # __name__ = '__main__'
####################################


# ------------
# END POINT-1: http://127.0.0.1:5000/ URL MAPPED TO route('/')
##############
@my_website_app.route("/")
def my_index_page():
    return "Welcome"
####################################


# ------------
# Run builtin server
##############
my_website_app.run(debug=True)
# my_website_app.run(debug=True, host='', port='')
####################################