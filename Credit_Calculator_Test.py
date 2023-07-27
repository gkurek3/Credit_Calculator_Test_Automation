import time
import Excel_Utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # prevents browser from shutting down
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.totalmoney.pl/kalkulatory/kredyt-gotowkowy-kalkulator-rat")
driver.maximize_window()
time.sleep(2)

# Deals with accepting cookies pop up
driver.find_element(By.XPATH, "//button[contains(text(),'AKCEPTUJĘ I PRZECHODZĘ DO SERWISU')]").click()

file = r"C:\Users\gkure\PycharmProjects\Credit_Calculator_Test_Automation\Credit_Calculator_Test_Cases.xlsx"
rows = Excel_Utils.get_row_count(file, "Arkusz1")  # gets total number of rows in Excel file

for r in range(2, rows + 1):
    # getting the data from Excel file
    tc_credit_value = Excel_Utils.read_data(file, "Arkusz1", r, 1)
    tc_credit_period = Excel_Utils.read_data(file, "Arkusz1", r, 2)
    tc_credit_percentage = Excel_Utils.read_data(file, "Arkusz1", r, 3)
    tc_expected_monthly = Excel_Utils.read_data(file, "Arkusz1", r, 4)

    # passing the data to the application
    driver.find_element(By.XPATH, "//input[@id='credit-value']").send_keys(tc_credit_value)
    driver.find_element(By.XPATH, "//input[@id='credit-period']").send_keys(tc_credit_period)
    driver.find_element(By.XPATH, "//input[@id='credit-intrest']").send_keys(tc_credit_percentage)
    driver.find_element(By.XPATH, "//span[contains(text(),'Oblicz ratę kredytu')]").click()
    time.sleep(2)

    result = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div[1]/div/div/h3").text
    result_cut = result.split(' z')[0]
    result_cut = result_cut.split(': ')[1]
    result_cut2 = result_cut.replace(" ", "")
    result_cut3 = result_cut2.replace(",", ".")
    result_cut4 = float(result_cut3)

    # validation
    if tc_expected_monthly == result_cut4:
        print("test passed")
        Excel_Utils.write_data(file, "Arkusz1", r, 6, "Pass")
        Excel_Utils.fill_green_color(file, "Arkusz1", r, 6)
    else:
        print("test failed")
        Excel_Utils.write_data(file, "Arkusz1", r, 6, "Fail")
        Excel_Utils.fill_red_color(file, "Arkusz1", r, 6)
