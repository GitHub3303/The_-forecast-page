import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from forecast_page.base.base_action import BaseAction


class Find_Page(BaseAction):
    #查找元素：9-day forecast
    forecast = By.XPATH, "//*[contains(@text,'9-day forecast')]"

    def click_more(self):
        self.click(self.forecast)
