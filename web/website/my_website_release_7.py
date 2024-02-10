"""
added 'addnewuser' endpoint
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
# END POINT-5: http://127.0.0.1:5000/register URL MAPPED TO route('/register')
##############
@my_website_app.route("/register")
def my_register_page():
    return flask.render_template("register.html")
####################################


# ------------
# END POINT-6: http://127.0.0.1:5000/addnewuser URL MAPPED TO route('/addnewuser')
##############
@my_website_app.route("/addnewuser", methods=['POST'])
def my_addnewuser_page():
    """
    Our Plan:
    Task-1: Get all new user details
    Task-2: Check whether both the passwords are matching
    Task-3: Create database and table
    Task-4: Check whether user already present in database
    Task-5: add new user details to database
    """
    # ------------
    # Task-1: Get all new user details
    ##############
    # flask is keeping all form data in a dictionary
    # flask.request.form = {uname: entered username, pw1: entered password, }
    entered_username = flask.request.form.get("uname")
    entered_password_1 = flask.request.form.get("pw1")
    entered_password_2 = flask.request.form.get("pw2")
    entered_email = flask.request.form.get("email")
    ####################################

    # ------------
    # Task-2: Check whether both the passwords are matching
    ##############
    if entered_password_1 != entered_password_2:
        return "Both the passwords are not matching.<br><a href='/register'>Go Back</a>"
    ####################################

    # ------------
    # Task-3: Create database and table
    ##############
    import sqlite3
    my_db_connection = sqlite3.connect("my_users_db.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = """
    CREATE TABLE IF NOT EXISTS MY_USERS_TABLE(
    USERNAME VARCHAR(100),
    PASSWORD VARCHAR(100),
    EMAIL VARCHAR(100)
    )
    """
    my_db_cursor.execute(my_query)
    ####################################

    # ------------
    # Task-4: Check whether user already present in database
    ##############
    my_query = f"SELECT COUNT(*) FROM MY_USERS_TABLE WHERE USERNAME='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone() # example if 10 records are present then (10,)
    users_count = my_db_result[0] # 10
    if users_count > 0:
        return "User Already Exists.<br><a href='/register'>Go Back</a>"
    ####################################

    # ------------
    # Task-5: add new user details to database
    ##############
    my_query = f"INSERT INTO MY_USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "Account Created.<br><a href='/login'>Login Here</a>"
    ####################################

####################################

# ------------
# Run builtin server
##############
my_website_app.run(debug=True)
# my_website_app.run(debug=True, host='', port='')
####################################