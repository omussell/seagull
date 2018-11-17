from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.headless = True
        self.browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
    #    self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
