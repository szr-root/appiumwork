from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testweinxin:
    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '。launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_weixin(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b78' and @index='2']").send_keys("李四")
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b81' and @text='男']").click()
        man_element = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='男']")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(man_element))
        man_element.click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys("17780694751")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        self.driver.back()

        men_elment = self.driver.find_elements(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dza']")
        mem_list=[]
        for men in men_elment:
                mem_list.append(men)

        assert "李四" in mem_list
