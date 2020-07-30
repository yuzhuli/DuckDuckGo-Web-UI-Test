import pytest
import json

from selenium import webdriver

# scope is session. so the fixture is run only once for the entire testing session
@pytest.fixture(scope='session')
def config():
    with open('./config.json') as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def validate_browser(config):
    if 'browser' not in config:
        raise Exception('Missing browser info in config')
    if config['browser'] not in {'chrome', 'safari'}:
        raise Exception(f"'{config['browser']}' is not a supported browser")
    return config['browser']

@pytest.fixture(scope='session')
def validate_wait_time(config):
    if 'wait_time' not in config:
        return 10
    return config['wait_time']

@pytest.fixture
def browser(validate_browser, validate_wait_time):
    if validate_browser == 'chrome':
        driver = webdriver.Chrome('./chromedriver')
    elif validate_browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise Exception(f"{config['browser']} is not a supported browser")

    driver.implicitly_wait(validate_wait_time)
    yield driver
    driver.quit()