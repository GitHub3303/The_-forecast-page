import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
from forecast_page.base.base_driver import init_driver
from forecast_page.page.click_list import ListPage

class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_List = ListPage(self.driver)


    def test_mobile_display_input(self):
        # 点击列表
        self.display_List.click()
