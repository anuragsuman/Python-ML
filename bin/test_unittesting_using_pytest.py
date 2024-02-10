"""
pytest: Library for unit testing
"""

'''
pytest Instructions
- file name should startswith test_
- write separate function for each test case
- each function name should startswith test_
- validate/verify the result using 'assert' instead of 'if/else'
'''

# Test Case-1:
def test_add_test():
    a = 10
    b = 20
    c = a + b
    assert c == 30
    assert c > 10
    assert c < 100
    #
    # if condition true then dont do anything else throw assertion error
    # If any test case returning assertion Error then framework will treat that test
    # case is failed

    #
    # Don't Do this, instead use 'assert'
    # if c == 30:
    #     print("Test Case Success")
    # else:
    #     print("Test case Failed")


# Test Case -2 : test course name in mymodule.py
from mymodule import course
def test_mymodule_course():
    assert course == "Python"
    assert len(course) > 0

# Test Case - 3: test log_process_kw_arg_func
from mymodule import log_process_kw_arg_func
def test_log_process_kw_arg_func():
    log_result = log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
    assert len(log_result) > 0

# Test Case - 4: test MyLogProcessClass
from  mymodule import MyLogProcessClass

def test_MyLogProcessClass():
    my_class_obj = MyLogProcessClass("../log/server_log.txt")
    ips_list = my_class_obj.get_ips()
    assert len(ips_list) > 0

# Test Case - 5 : test google search
def test_google_search():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    # Step-1: Open the browser
    my_web_browser = webdriver.Edge()

    # Step-2: Type the URL
    my_web_browser.get("https://www.google.com")

    # Step-3: Findout search box
    google_search_field = my_web_browser.find_element(by='name', value='q')

    # Step-4: Type 'Python'
    google_search_field.send_keys("Python")

    # Step-5: Press Enter
    google_search_field.send_keys(Keys.RETURN)

    # Step-6: Check whether word 'Python' present in browser title
    # - We usually validate result using 'assert' statement instead of
    #   if/else
    assert "Python" in my_web_browser.title


# COMMAND TO EXECUTE TEST CASES
# pytest -v test_unittesting_using_pytest.py