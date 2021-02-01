from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.base_page import BasePage
from appium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    def click_contact(self):
        self.find((MobileBy.XPATH, "//*[@text='通讯录']"))
        return ContactPage(self.driver)