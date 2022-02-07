from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == "firefox":
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif browser == "ie":
        driver = webdriver.Ie(executable_path="C:\\wd-drivers\\IEDriverServer.exe")
    elif browser == "edge":
        driver = webdriver.Edge(executable_path="C:\\wd-drivers\\msedgedriver.exe")
    else:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    return driver


def pytest_addoption(parser):  # This will fetch value from command line
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return browser value to setup function
    return request.config.getoption("--browser")


#################Pytest HTML Report###########################
# Hook for adding environment info in html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'saucedemo'
    config._metadata['Mpdule Name'] = 'Homepage'
    config._metadata['QA Name'] = 'Amit P.'


# Hook to delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

