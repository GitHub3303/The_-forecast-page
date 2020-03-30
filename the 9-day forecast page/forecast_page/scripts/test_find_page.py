import os, sys
sys.path.append(os.getcwd())

from forecast_page.base.base_driver import init_driver
from forecast_page.page.find_page import Find_Page


class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.find_page = Find_Page(self.driver)


    def test_mobile_network_3g(self):
        self.find_page.click_more()
