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
        window_handles1 = driver.window_handles
        print(len(window_handles1))
        print('p2')
        for wh1 in window_handles1:
            print(wh1)
        # clicking Help Button will open Help Page in a new Popup
        # Browser Window
        help_button = driver.find_element_by_id("chatbutton")
        help_button.click()
        
        window_handles2 = driver.window_handles
        print(type(window_handles2))
        print(len(window_handles2))
        for wh2 in window_handles2:
            print(wh2)
        wh_popup = window_handles2[1]
        time.sleep(7)
        driver.switch_to.window(wh_popup)
        time.sleep(5)
        close_button = driver.find_element_by_id("closebutton")
        close_button.click()
        #driver.close()
        #driver.switch_to.window(parent_window_id)
                


    
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

