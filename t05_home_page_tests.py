import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # create a new session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        
        # navigate to the application home page
        cls.driver.get("http://www.viosta.com/mag/")
    
    @classmethod    
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
        
        
    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        products_number = len(products)
        
        #for product in products:
        #    print(product.text)
        self.assertEqual(3, products_number, 'not 3 products')
        
    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("Swing")
        self.search_field.submit()
        # get all the anchor elements which have
        # product names displayed
        # currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))
                
if __name__ == '__main__':
    unittest.main(verbosity=2)