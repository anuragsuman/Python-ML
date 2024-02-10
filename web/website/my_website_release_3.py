"""
added index.html
"""

# ------------
# Where to keep all html files
##############
# - create a directory 'templates' inside website folder
# - inside 'templates', keep all html files
####################################


# ------------
# Create app for our website
##############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__) # __name__ = '__main__'
####################################


# # ------------
# # END POINT-1: http://127.0.0.1:5000/ URL MAPPED TO route('/')
# ##############
# @my_website_app.route("/")
# def my_index_page():
#     return "Welcome"
# ####################################


# ------------
# END POINT-2: http://127.0.0.1:5000/ URL MAPPED TO route('/')
##############
@my_website_app.route("/")
def my_index_page():
    return flask.render_template("index.html")
####################################


# ------------
# Run builtin server
##############
my_website_app.run(debug=True)
# my_website_app.run(debug=True, host='', port='')
####################################