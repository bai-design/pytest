import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def open_driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(params=["https://renren.com/"], ids=["测试人人网"])
def get_url(open_driver,request):
    open_driver.get(request.param)
    yield open_driver
    print(f'请求地址: {request.param}')

def pytest_collection_modifyitems(session, config, items):
    items.reverse()
    for item in items:
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        if "default" in item.nodeid:
            item.add_marker(pytest.mark.miss)
