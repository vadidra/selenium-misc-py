from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class ToolTipTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        #self.driver.get("http://www.viosta.com/mag/")
        self.driver.get("http://jqueryui.com/resources/demos/droppable/default.html")
        
    def test_drag_and_drop(self):
        driver = self.driver
        source = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("droppable")
        time.sleep(5)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        time.sleep(7)
        self.assertEqual("Dropped!", target.text)
        


    
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

