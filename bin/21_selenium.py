"""
Web Application Testing using selenium
"""

'''
Test Case: Check whether google search is working or not?

Steps:
Step-1: Open the browser
Step-2: Type the URL
Step-3: Findout search box
Step-4: Type 'Python'
Step-5: Press Enter
Step-6: Check whether word 'Python' present in browser title
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Step-1: Open the browser
my_web_browser = webdriver.Chrome()

# Step-2: Type the URL
my_web_browser.get("https://www.google.com")

# Step-3: Findout search box
google_search_field = my_web_browser.find_element(by='name', value='q')

# Step-4: Type 'Python'
google_search_field.send_keys("anurag")

# Step-5: Press Enter
google_search_field.send_keys(Keys.RETURN)

# Step-6: Check whether word 'Python' present in browser title
# - We usually validate result using 'assert' statement instead of
#   if/else
assert "anurag" in my_web_browser.title
# - assert will check the given condition, if it fails then it throws error
print("Test Case Success")
my_web_browser.close()