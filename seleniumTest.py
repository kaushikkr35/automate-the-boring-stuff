from selenium import webdriver as wbd
browser = wbd.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with class name!' % (elem.tag_name))
except:
    print('Could not find the element')
