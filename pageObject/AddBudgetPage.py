from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage

class AddBudgetPage(BasePage):
    budget_type = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText')
    budget_value = (MobileBy.ID, 'protect.budgetwatch:id/value')
    save_button = (MobileBy.ID, 'protect.budgetwatch:id/saveButton')
    msg_error = ('protect.budgetwatch:id/snackbar_text')

    def enter_budget_type(self, text):
        budget_type_element = self.driver.find_element(*AddBudgetPage.budget_type)
        budget_type_element.send_keys(text)

    def enter_budget_value(self, text):
        budget_value_element = self.driver.find_element(*AddBudgetPage.budget_value)
        budget_value_element.send_keys(text)

    def click_budget_value(self):
        budget_value_element = self.driver.find_element(*AddBudgetPage.budget_value)
        budget_value_element.click()

    def click_save_button(self):
        save_element = self.driver.find_element(*AddBudgetPage.save_button)
        save_element.click()

    def get_error(self):
        error_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((
        MobileBy.ID, self.msg_error)))
        return error_element.text


