from selenium import webdriver
import unittest
import time

class Login(unittest.TestCase):

    def setUp(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://cn.bing.com/")

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__=="__main__":
        unittest.main()