from frame.baseconfig.app import App


class TestFrame:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_frame(self):
        result = self.main.goto_market().get_market_page()
        assert result
