from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.base_page import BasePage
from appium_po.page.memedit_page import MemEditPage


class AddMemberPage(BasePage):
    def click_addmember_manual(self):
        return MemEditPage(self.driver)

    def get_toast(self):
        ele = self.find((MobileBy.XPATH, '//*[@class="android.widget.Toast"]')).text
        return ele
