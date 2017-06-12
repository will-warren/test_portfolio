from selenium import webdriver
import unittest
import time
import re


class PortfolioTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://willwile4.github.io/')
        self.assertIn('Will Warren 4', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
