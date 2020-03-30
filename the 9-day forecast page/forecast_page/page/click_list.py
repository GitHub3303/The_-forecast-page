from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class ListPage(BaseAction):

    # 查找菜单列表
    list_button = By.ID, "com.android.settings:id/list"

    def __init__(self, driver):

        BaseAction.__init__(self, driver)
        self.click_display()
    #点击=列表
    def click_text_view(self):
        # self.driver.find_element(self.input_text_view).click()
        self.click(self.list_button)
