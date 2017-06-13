from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import re


class PortfolioTestChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    # def testPageTitle(self):
    #     '''tests correct page title'''
    #     self.driver.get('https://willwile4.github.io/')
    #     self.assertIn('Will Warren 4', self.driver.title)

    # def testDesktopLinkText(self):
    #     '''tests correct text on large screen (>768px) navigation links'''
    #     self.driver.get('https://willwile4.github.io/')
    #     nav_li= [li.text for li in self.driver.find_elements(By.ID,
    #                                                           'nav-list')]
    #     nav_li = nav_ul[0].split('\n')
    #     self.assertIn('GitHub', nav_li)
    #     self.assertIn('Resume', nav_li)
    #     self.assertIn('LinkedIn', nav_li)
    #     self.assertIn('Instagram', nav_li)

    def testGitHubDesktop(self):
        '''tests github link goes to my GitHub'''
        self.driver.get('https://willwile4.github.io')
        nav = self.driver.find_element(By.ID, 'nav-list')
        print(nav.text, 'line 34')

    # def testMobileLinks(self):
    #     '''tests correct image on small screen (<768px) navigation links'''
    #     self.driver.get('https://willwile4.github.io/')
    #     nav = self.driver.find_element(By.ID, 'mobile-nav')
    #     print(nav)

    # def testPortfolio(self):
    #     '''tests portfolio item buttons'''
    #     pass
    #
    # def testAccordian(self):
    #     '''tests accordian functionality'''
    #     pass
    #
    # def testResponsive(self):
    #     '''tests that page switches to mobile view below 768px'''
    #     pass

    # def tearDown(self):
    #     self.driver.quit()


# class PortfolioTestFirefox(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#
# class PortfolioTestSafari(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#
# class PortfolioTestOpera(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#
# class PortfolioTestIE(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#
# class PortfolioTestAndroid(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#
# class PortfolioTestiOS(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
