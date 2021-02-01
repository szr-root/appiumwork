from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.addmember_page import AddMemberPage
from appium_po.page.base_page import BasePage


class ContactPage(BasePage):
    def click_addmenber(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector().'
                                  'scrollable(true).instance(0)).'
                                  'scrollIntoView(new UiSelector().'
                                  'text("添加成员").instance(0));').click()
        return AddMemberPage(self.driver)
