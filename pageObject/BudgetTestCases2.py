import unittest
from MainPage import MainPage
from BudgetPage import BudetPage
from AddBudgetPage import AddBudgetPage
from appium import webdriver


class MyTestCase(unittest.TestCase):
    BUDGET_TYPE = 'lanche'
    BUDGET_VALUE = '500'
    ERROR_BUDGET_TYPE = 'Budget type is empty'
    ERROR_BUDGET_VALUE = 'Budget value is empty'

    def setUp(self):
        "configurar teste"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = 'emulator-5554'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        self.driver = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps)

    def test_adicionar_orcamento_valido(self):
        main_page = MainPage(self.driver)
        main_page.click_budgets()
        budget_page = BudetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        add_page.enter_budget_type(self.BUDGET_TYPE)
        add_page.enter_budget_value(self.BUDGET_VALUE)
        add_page.click_save_button()
        #budget_page = BudetPage(self.driver)
        assert self.BUDGET_TYPE in budget_page.get_first_budget()

    def test_adicionar_orcamento_sem_nome(self):
        main_page = MainPage(self.driver)
        main_page.click_budgets()
        budget_page = BudetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        add_page.click_budget_value(self.driver)
        add_page.enter_budget_value(self.BUDGET_VALUE)
        add_page.click_save_button()
        assert self.ERROR_BUDGET_TYPE in add_page.get_error()

    def test_adicionar_orcamento_sem_valor(self):
        main_page = MainPage(self.driver)
        main_page.click_budgets()
        budget_page = BudetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        add_page.enter_budget_type(self.BUDGET_TYPE)
        add_page.click_save_button()
        assert self.ERROR_BUDGET_VALUE in add_page.get_error()


if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    #unittest.TextTestRunner(verbosity=2).run(suite)

