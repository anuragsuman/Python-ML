"""
added login.html
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
# END POINT-3: http://127.0.0.1:5000/about URL MAPPED TO route('/about')
##############
@my_website_app.route("/about")
def my_about_page():
    return flask.render_template("about.html")
####################################


# ------------
# END POINT-4: http://127.0.0.1:5000/login URL MAPPED TO route('/login')
##############
@my_website_app.route("/login")
def my_login_page():
    return flask.render_template("login.html")
####################################

# ------------
# Run builtin server
##############
my_website_app.run(debug=True)
# my_website_app.run(debug=True, host='', port='')
####################################