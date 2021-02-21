import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from frame_yaml.config.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def send(self, locator, content):
        self.find(locator).send_keys(content)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find(element).click()

    def step(self, path, operation):
        with open(path, 'r', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            # yaml中定义操作方式
            steps = datas[operation]
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if action == "find_and_click":
                    self.find_and_click(step["locator"])
                elif action == "send":
                    self.send(step["locator"], step["text"])

