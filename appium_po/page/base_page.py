from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)
