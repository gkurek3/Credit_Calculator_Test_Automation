from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebdriverSetup:
    @staticmethod
    def webdriver_setup():
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # prevents browser from shutting down
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        driver.get("https://www.totalmoney.pl/kalkulatory/kredyt-gotowkowy-kalkulator-rat")
        driver.maximize_window()
        return driver
    