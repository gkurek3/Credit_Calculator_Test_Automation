from PageObject.Config.Excel_path import file
from PageObject.Excel_Config import Excel_Utils


class ExcelSupport:
    def __init__(self):
        rows = Excel_Utils.get_row_count(file, "Arkusz1")  # gets total number of rows in Excel file

        for row in range(2, rows + 1):
            # getting the data from Excel file
            self.tc_credit_value = Excel_Utils.read_data(file, "Arkusz1", row, 1)
            self.tc_credit_period = Excel_Utils.read_data(file, "Arkusz1", row, 2)
            self.tc_credit_percentage = Excel_Utils.read_data(file, "Arkusz1", row, 3)
            self.tc_expected_monthly = Excel_Utils.read_data(file, "Arkusz1", row, 4)
