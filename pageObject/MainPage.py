from appium.webdriver.common.mobileby import MobileBy
from BasePage import BasePage

class MainPage(BasePage):

    budgets = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')

    def click_budgets(self):
        budgets_element = self.driver.find_element(*MainPage.budgets)
        budgets_element.click()

    #def click_transactions(self):
    #    self.transactions.click()

