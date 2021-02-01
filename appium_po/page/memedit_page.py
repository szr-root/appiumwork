from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage


class MemEditPage(BasePage):
    def edit_name(self,name):
        self.find((
            MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")).\
            send_keys(name)
        return self

    def edit_gender(self,gender):
        man_element = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(man_element))
        ele.click()
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        return self

    def edit_phonenum(self,phonenum):
        self.find((MobileBy.ID, "com.tencent.wework:id/eq7")).send_keys(phonenum)
        return self

    def click_saves(self):
        from appium_po.page.addmember_page import AddMemberPage
        self.find((MobileBy.ID, "com.tencent.wework:id/gur")).click()
        return AddMemberPage(self.driver)
