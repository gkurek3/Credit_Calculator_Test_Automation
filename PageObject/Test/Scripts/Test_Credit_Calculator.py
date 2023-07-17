import time
import unittest

import Excel_Utils
from PageObject.Pages.Credit_Calculator_Page import CreditCalculatorPage
from PageObject.Config.WebdriverSetup import WebdriverSetup
from PageObject.Config.Excel_path import file


class TestCreditCalculator(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebdriverSetup.webdriver_setup()
        self.page_object = CreditCalculatorPage(self.driver)
        time.sleep(2)
        self.page_object.click_pop_up_button()

    def test_page_title(self):
        web_page_title = "Kalkulator kredytowy gotówkowy 2023 – kalkulator rat kredytu gotówkowego"
        assert self.driver.title == web_page_title

    def test_credit_result(self):
        rows = Excel_Utils.get_row_count(file, "Arkusz1")  # gets total number of rows in Excel file

        for row in range(2, rows + 1):
            # getting the data from Excel file
            tc_credit_value = Excel_Utils.read_data(file, "Arkusz1", row, 1)
            tc_credit_period = Excel_Utils.read_data(file, "Arkusz1", row, 2)
            tc_credit_percentage = Excel_Utils.read_data(file, "Arkusz1", row, 3)
            tc_expected_monthly = Excel_Utils.read_data(file, "Arkusz1", row, 4)

            self.page_object.credit_value().send_keys(tc_credit_value)
            self.page_object.credit_period().send_keys(tc_credit_period)
            self.page_object.credit_interest().send_keys(tc_credit_percentage)

            self.page_object.calculate_button().click()
            time.sleep(2)

            result = self.page_object.result().text
            result_cut = result.split(' z')[0]
            result_cut = result_cut.split(': ')[1]
            result_cut2 = result_cut.replace(" ", "")
            result_cut3 = result_cut2.replace(",", ".")
            result_cut4 = float(result_cut3)

            # validation
            if tc_expected_monthly == result_cut4:
                print("test passed")
                Excel_Utils.write_data(file, "Arkusz1", row, 6, "Pass")
                Excel_Utils.fill_green_color(file, "Arkusz1", row, 6)
            else:
                print("test failed")
                Excel_Utils.write_data(file, "Arkusz1", row, 6, "Fail")
                Excel_Utils.fill_red_color(file, "Arkusz1", row, 6)
