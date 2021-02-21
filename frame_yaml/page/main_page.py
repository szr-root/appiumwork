from frame_yaml.config.base_page import BasePage
from frame_yaml.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search_page(self):
        # self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        self.step("../page/main_page.yaml", "goto_search")
        return SearchPage(self.driver)
