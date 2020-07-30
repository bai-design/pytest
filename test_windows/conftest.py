import pytest
from selenium import webdriver
import os
import yaml

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

def pytest_collection_modifyitems(items):
    items.reverse()
    for item in items:
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        if "default" in item.nodeid:
            item.add_marker(pytest.mark.miss)

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="test")

def pytest_configure(config):
    os.environ["env"] = config.getoption("--env", default="test")

@pytest.fixture(scope="function")
def test_read_env():
    if os.environ["env"] == "test":
        info = yaml.safe_load(open(file="./test.yml"))
    else:
        info = yaml.safe_load(open(file="./produce.yml"))
    return info
