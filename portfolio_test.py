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
        '''tests correct page title'''
        self.driver.get('https://willwile4.github.io/')
        self.assertIn('Will Warren 4', self.driver.title)

    # testing desktop links for correct text and destination
    def testGitHubLinkText(self):
        '''tests github link text on large screen (>768px) '''
        self.driver.get('https://willwile4.github.io')
        nav = self.driver.find_element(By.ID, 'github-lg')
        self.assertIn('GitHub', nav.text)

    def testGitHubDesktop(self):
        '''tests github link goes to my GitHub on large screen (>768px) '''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'github-lg').click()
        self.assertEqual(self.driver.current_url,
                          'https://github.com/willwile4')

    def testLinkdInLinkText(self):
        '''tests linkedIn link text on large screen (>768px) '''
        self.driver.get('https://willwile4.github.io')
        nav = self.driver.find_element(By.ID, 'linkedin-lg')
        self.assertIn('LinkedIn', nav.text)

    # Doesn't view public profile, instead redirects for login

    # def testLinkedInDesktop(self):
    #     '''tests github link goes to my LinkedIn on large screen (>768px) '''
    #     self.driver.get('https://willwile4.github.io')
    #     self.driver.find_element(By.ID, 'linkedin-lg').click()
    #     self.assertEqual(self.driver.current_url,
    #                       'https://www.linkedin.com/in/willwarren4')

    def testResumeLinkText(self):
        '''tests resume link text on large screen (>768px) '''
        self.driver.get('https://willwile4.github.io')
        nav = self.driver.find_element(By.ID, 'resume-lg')
        self.assertIn('Resume', nav.text)

    def testResumeDesktop(self):
        '''tests resume link loads my resume on large screen (>768px) '''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'resume-lg').click()
        self.assertEqual(self.driver.title, 'Will_Warren_Resume.pdf')

    def testInstagramLinkText(self):
        '''tests instgram link text on large screen (>768px)'''
        self.driver.get('https://willwile4.github.io')
        nav = self.driver.find_element(By.ID, 'insta-lg')
        self.assertIn('Instagram', nav.text)

    def testInstagramDesktop(self):
        '''tests instagram like goes to my ig on large screen (>768px)'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'insta-lg').click()
        self.assertEqual(self.driver.current_url,
                         'https://www.instagram.com/willwile4/')

    # testing mobile links
    # it is assumed that if the driver finds the css image class
    # then the correct image is displayed.
    def testGitHubSmallScreen(self):
        '''tests GitHub css image link on small screen (<768px)'''
        self.driver.get('https://willwile4.github.io')
        self.driver.set_window_size(400, 600)
        nav = self.driver.find_elements(By.CLASS_NAME, 'soc-github')
        nav[0].click()
        self.assertEqual(self.driver.current_url,
                         'https://github.com/willwile4')

    def testLinkedInSmallScreen(self):
        '''tests LinkedIn css image link on small screen (<768px)'''
        self.driver.get('https://willwile4.github.io')
        self.driver.set_window_size(400, 600)
        nav = self.driver.find_elements(By.CLASS_NAME, 'soc-linkedin')
        nav[0].click()
        self.assertEqual(self.driver.current_url,
                         'https://www.linkedin.com/in/willwarren4/')

    # doesn't yet open public profile. 
    def testInstagramSmallScreen(self):
        '''tests Instagram css image link on small screen (<768px)'''
        self.driver.get('https://willwile4.github.io')
        self.driver.set_window_size(400, 600)
        nav = self.driver.find_elements(By.CLASS_NAME, 'soc-instagram')
        nav[0].click()
        self.assertEqual(self.driver.current_url,
                         'https://www.instagram.com/willwile4/')

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
