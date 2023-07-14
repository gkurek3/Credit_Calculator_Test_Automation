import unittest

from PageObject.Pages.Credit_Calculator_Page import CreditCalculatorPage
from PageObject.Config.WebdriverSetup import WebdriverSetup


class TestCreditCalculator(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebdriverSetup.webdriver_setup()
        self.page_object = CreditCalculatorPage(self.driver)

    def test_page_title(self):
        web_page_title = "Kalkulator kredytowy gotówkowy 2023 – kalkulator rat kredytu gotówkowego"
        assert self.driver.title == web_page_title
