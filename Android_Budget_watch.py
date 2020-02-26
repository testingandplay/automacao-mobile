import unittest, time, os
from appium import webdriver
import thread
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    LANCHE= "lanche"

    def setUp(self):
        "configurar teste"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = ''
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_adicionar_orcamento_valido(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
        el1.click()
        el2 = self.driver.find_element_by_accessibility_id("Add")
        el2.click()
        el3= self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText")
        el3.send_keys("lanche")
        el4 = self.driver.find_element_by_id("protect.budgetwatch:id/value")
        el4.send_keys("500")
        el5 = self.driver.find_element_by_id("protect.budgetwatch:id/saveButton")
        el5.click()
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView")
        path= el6.text
        assert "lanche" in path

    def test_adicionar_orcamento_sem_valor(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
        el1.click()
        el2 = self.driver.find_element_by_accessibility_id("Add")
        el2.click()
        el3 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText")
        el3.send_keys("lanche")
        el5 = self.driver.find_element_by_id("protect.budgetwatch:id/saveButton")
        el5.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((
                       MobileBy.ID, "protect.budgetwatch:id/snackbar_text")))


if __name__ == '__main__':
    unittest.main()
