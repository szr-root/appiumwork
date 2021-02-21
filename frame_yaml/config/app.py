from appium import webdriver

from frame_yaml.config.base_page import BasePage
from frame_yaml.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.1.2'
            desired_caps['deviceName'] = '127.0.0.1:21503'
            desired_caps["appPackage"] = "com.xueqiu.android"
            desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
            desired_caps['noReset'] = 'true'
            # desired_caps['dontStopAppOnReset'] = 'true'
            # desired_caps['skipDeviceInitialization'] = 'true'
            # desired_caps['unicodeKeyboard'] = 'true'
            # desired_caps['resetKeyboard'] = 'true'
            desired_caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间为0秒
            desired_caps['settings[waitForIdleTimeout]'] = 1
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
