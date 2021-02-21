from frame_yaml.config.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_frame(self):
        result = self.main.goto_search_page().search()
        assert result
