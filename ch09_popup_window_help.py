from selenium import webdriver
import unittest
import time

class PopupWindowTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://rawgit.com/upgundecha/learnsewithpython/master/pages/Config.html")
    
    

    def test_window_popup(self):
        driver = self.driver
        # save the WindowHandle of Parent Browser Window
        parent_window_id = driver.current_window_handle
        # clicking Help Button will open Help Page in a new Popup
        # Browser Window
        help_button = driver.find_element_by_id("helpbutton")
        help_button.click()
        time.sleep(7)
        driver.switch_to.window("HelpWindow")
        time.sleep(5)
        driver.close()
        driver.switch_to.window(parent_window_id)
                


    
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

