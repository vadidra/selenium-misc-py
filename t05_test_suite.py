import unittest

from t04_search_tests_class import SearchTests
from t05_home_page_tests import HomePageTests

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
