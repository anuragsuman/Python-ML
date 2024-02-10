"""
Flask framework for developing RESTFul web services
"""

'''
Suppose i need to share log data table with others/public
how to share?

OPTION-1: provide host, port, user name, password etc to others/public

OPTION-1 will not work 

OPTION-1 is like
our-app/our-data    <-DIRECT ENTRY-> others/public
'''

'''
We got 
OPTION-2

2 OPTIONS we got
1) SOAP
2) REST

both tells don't give direct access, instead introduce some GATE/INTERFACE in between

OPTION-2 is like
our-app/our-data    <-- GATE/INTERFACE ---> others/public

- APPLICATION PROGRAMMING INTERFACE (API)
SOAP-API
REST-API
'''

'''
- REST & SOAP are called designs/architectures/style
- REST & SOAP will tell how to write such interface
- REST came after SOAP
- REST is easy to implement and manage
- REST is popular
'''

'''
i need to share log data table with others/public
using REST then how write program to create REST INTERFACE?

- Answer: No Need to write REST INTERFACE from scratch
BECAUSE
flask is already implemented REST
'''

'''
i need to share log data table with others/public
using flask then how to REST-API?

Steps
1. create flask app
2. create endpoint
3. pull log data from db
4. return log data in json
5. run the server
6. share END POINT URL with others/public
so that they can access through that endpoint

'''

# ------------
# Create app for our website
##############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__) # __name__ = '__main__'
####################################


# ------------
# REST API END POINT: http://127.0.0.1:5000/ URL MAPPED TO route('/')
##############
@my_website_app.route("/")
def my_rest_api():
    """
    REST API TO EXPOSE LOG DATA
    """
    import sqlite3
    my_db_connection = sqlite3.connect(r"../../programs/my_data_db.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = "SELECT * FROM MY_DATA_TABLE"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
####################################

# ------------
# Run builtin server
##############
my_website_app.run(debug=True)
# my_website_app.run(debug=True, host='', port='')
####################################