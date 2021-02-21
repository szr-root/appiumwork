from frame_yaml.config.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.step("../page/search_page.yaml", "search")
        return True
