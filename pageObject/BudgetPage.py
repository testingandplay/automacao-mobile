from appium.webdriver.common.mobileby import MobileBy
from BasePage import BasePage

class BudetPage(BasePage):

    add = (MobileBy.ACCESSIBILITY_ID, 'Add')
    first_budget = (MobileBy.XPATH,
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView')

    def click_add(self):
        add_element = self.driver.find_element(*BudetPage.add)
        add_element.click()

    def get_first_budget(self):
        first_budget_element = self.driver.find_element(*BudetPage.first_budget)
        return first_budget_element.text
