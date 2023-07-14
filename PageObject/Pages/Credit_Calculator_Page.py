from PageObject.Locators.Locator import Locator
from selenium.webdriver.common.by import By


class CreditCalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_pop_up_button(self):
        return self.driver.find_element(By.XPATH, Locator.pop_up_button)

    def credit_value(self):
        return self.driver.find_element(By.XPATH, Locator.credit_value)

    def credit_period(self):
        return self.driver.find_element(By.XPATH, Locator.credit_period)

    def credit_interest(self):
        return self.driver.find_element(By.XPATH, Locator.credit_interest)

    def calculate_button(self):
        return self.driver.find_element(By.XPATH, Locator.calculate_button)

    def result(self):
        return self.driver.find_element(By.XPATH, Locator.result)
