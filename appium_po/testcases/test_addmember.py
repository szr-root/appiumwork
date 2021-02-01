import pytest
import yaml

from appium_po.page.app import App


def get_data():
    with open('./data.yaml', encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        return data


class TestAddMember:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_data())
    def test_addmember(self,name,gender,phonenum):
        toast = self.main.click_contact().click_addmenber("添加成员").click_addmember_manual().edit_name().\
            edit_gender().edit_phonenum().click_saves().get_toast()
        assert toast == "添加成功"

# if __name__ == '__main__':
#     print(get_data())
