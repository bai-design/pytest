import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def open_driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(params=["https://renren.com/"])
def get_url(open_driver,request):
    open_driver.get(request.param)
    yield open_driver
    print(f'请求地址: {request.param}')

