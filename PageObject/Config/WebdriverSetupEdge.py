from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebdriverSetupEdge:
    @staticmethod
    def webdriver_setup():
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        driver.get("https://www.totalmoney.pl/kalkulatory/kredyt-gotowkowy-kalkulator-rat")
        driver.maximize_window()
        return driver
