from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest


# TODO write tests for nav li hover color change
# TO FIX: button testing doesn't actually test buttons
#         LinkedIN doesn't open public profile page
class InvalidURLError(ValueError):
    pass


class PortfolioTestChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def validate_url(self, url):
        return self.driver.current_url == url

    def testPageTitle(self):
        '''tests correct page title'''
        self.driver.get('https://willwile4.github.io/')
        return EC.title_is('Will Warren 4')

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

    def testLinkedInDesktop(self):
        '''tests github link goes to my LinkedIn on large screen (>768px) '''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'linkedin-lg').click()
        self.assertEqual(self.driver.current_url,
                          'https://www.linkedin.com/in/willwarren4')

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

    # doesn't yet open a public profile
    def testLinkedInSmallScreen(self):
        '''tests LinkedIn css image link on small screen (<768px)'''
        self.driver.get('https://willwile4.github.io')
        self.driver.set_window_size(400, 600)
        nav = self.driver.find_elements(By.CLASS_NAME, 'soc-linkedin')
        nav[0].click()
        self.assertEqual(self.driver.current_url,
                         'https://www.linkedin.com/in/willwarren4/')


    def testInstagramSmallScreen(self):
        '''tests Instagram css image link on small screen (<768px)'''
        self.driver.get('https://willwile4.github.io')
        self.driver.set_window_size(400, 600)
        nav = self.driver.find_elements(By.CLASS_NAME, 'soc-instagram')
        nav[0].click()
        self.assertEqual(self.driver.current_url,
                         'https://www.instagram.com/willwile4/')

    # body
    def testBlurb(self):
        '''tests if blurb-box is visible'''
        return EC.presence_of_element_located((By.ID, 'blurb-box'))

    # test accordian UI
    def testAccordionOnLoad(self):
        '''tests portfolio-1 item is open on page load'''
        self.driver.get('https://willwile4.github.io')
        return (EC.presence_of_element_located((By.ID, 'p-lead-p')) and
        EC.presence_of_element_located((By.ID, 'p-lead-links')))

    def testAccordionLeadItem(self):
        '''tests portfolio-lead opens and previous item closes on click'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-2').click()
        self.driver.find_element(By.ID, 'portfolio-lead').click()
        return (EC.invisibility_of_element_located((By.ID, 'p2-p')) and
                EC.invisibility_of_element_located((By.ID, 'p2-links')) and
                EC.presence_of_element_located((By.ID, 'p-lead-p')) and
                EC.presence_of_element_located((By.ID, 'p-lead-links')))

    def testAccordionItem2(self):
        '''tests portfolio-1 item closes and portfolio-2 item opens on click'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-2').click()
        return (EC.invisibility_of_element_located((By.ID, 'p-lead-p')) and
                EC.invisibility_of_element_located((By.ID, 'p-lead-links')) and
                EC.presence_of_element_located((By.ID, 'p2-p')) and
                EC.presence_of_element_located((By.ID, 'p2-links')))

    def testAccordionItem3(self):
        '''tests portfolio-2 item closes and portfolio-3 item opens on click'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-3').click()
        return (EC.invisibility_of_element_located((By.ID, 'p2-p')) and
                EC.invisibility_of_element_located((By.ID, 'p2-links')) and
                EC.presence_of_element_located((By.ID, 'p3-p')) and
                EC.presence_of_element_located((By.ID, 'p3-links')))

    def testAccordionItem4(self):
        '''tests portfolio-3 item closes and portfolio-4 item opens on click'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-4').click()
        return (EC.invisibility_of_element_located((By.ID, 'p3-p')) and
                EC.invisibility_of_element_located((By.ID, 'p3-links')) and
                EC.presence_of_element_located((By.ID, 'p4-p')) and
                EC.presence_of_element_located((By.ID, 'p4-links')))

    # tests for each portfolio item. this isn't 'dynamic' information
    # but will change from time to time. tests should pass no matter the item
    def testPortfolioLeadBtns(self):
        '''tests portfolio lead item buttons, should be open on page load'''
        self.driver.get('https://willwile4.github.io')
        urls = [demo.get_attribute('href') for demo in
                self.driver.find_elements(By.XPATH,
                '//*[@id="p-lead-links"]//a')]
        # problem: this doesn't actually test button function. click() then
        # comparing urls raises a StaleElementException 6/14/17
        for url in urls:
            self.driver.get(url)
            self.assertEqual(self.driver.current_url, url)
            self.driver.back()

    def testPortfolioItem2Btns(self):
        '''tests portfolio item 2 buttons'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-2').click()
        urls = [demo.get_attribute('href') for demo in
                self.driver.find_elements(By.XPATH,
                '//*[@id="p2-links"]//a')]
        # problem: this doesn't actually test button function. click() then
        # comparing urls raises a StaleElementException 6/14/17
        for url in urls:
            self.driver.get(url)
            self.assertEqual(self.driver.current_url, url)
            self.driver.back()

    def testPortfolioItem3Btns(self):
        '''tests portfolio item 3 buttons'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-3').click()
        urls = [demo.get_attribute('href') for demo in
                self.driver.find_elements(By.XPATH,
                '//*[@id="p3-links"]//a')]
        # problem: this doesn't actually test button function. click() then
        # comparing urls raises a StaleElementException 6/14/17
        for url in urls:
            self.driver.get(url)
            self.assertEqual(self.driver.current_url, url)
            self.driver.back()

    def testPortfolioItem4Btns(self):
        '''tests portfolio item 4 buttons'''
        self.driver.get('https://willwile4.github.io')
        self.driver.find_element(By.ID, 'portfolio-4').click()
        urls = [demo.get_attribute('href') for demo in
                self.driver.find_elements(By.XPATH,
                '//*[@id="p4-links"]//a')]
        # problem: this doesn't actually test button function. click() then
        # comparing urls raises a StaleElementException 6/14/17
        for url in urls:
            self.driver.get(url)
            self.assertEqual(self.driver.current_url, url)
            self.driver.back()

    # test responsive layout
    def testResponsive(self):
        '''tests that page switches to mobile view below 768px'''
        self.driver.get('https://willwile4.github.io')
        size = self.driver.get_window_size()
        self.driver.set_window_size(size['width'] / 2, size['height'] / 2)
        return EC.presence_of_element_located((By.ID, 'mobile-nav'))

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
