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
        self.driver.get("http://jqueryui.com/tooltip/")
        
    def test_tool_tip(self):
        driver = self.driver
        frame_elm = driver.find_element_by_class_name("demo-frame")
        driver.switch_to.frame(frame_elm)
        age_field = driver.find_element_by_id("age")
        time.sleep(5)
        ActionChains(self.driver).move_to_element(age_field).perform()
        tool_tip_elm = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ui-tooltip-content")))
        # verify tooltip message
        time.sleep(5)
        self.assertEqual("We ask for your age only for statistical purposes.", tool_tip_elm.text)



    
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

