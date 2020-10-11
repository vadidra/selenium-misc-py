import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CompareProducts(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.viosta.com/mag/")
    
    def test_compare_products_removal_alert(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()
        # click the Add to compare link
        self.driver.find_element_by_link_text("Add to Compare").click()
        print(4)
        time.sleep(3)
        # click on Remove this item link, this will display
        # an alert to the user
        el1 = self.driver.find_element_by_link_text("Clear All")
        time.sleep(5)
        print(5)
        el1.click()
        print(6)
        time.sleep(5)
        # switch to the alert
        #alert = self.driver.switch_to_alert()
        alert = self.driver.switch_to.alert
        # get the text from alert
        alert_text = alert.text
        print(alert_text)
        # check alert text
        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
        # click on Ok button
        alert.accept()
                


    
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

