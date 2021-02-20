from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from frame.baseconfig.base_page import BasePage
from frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)
