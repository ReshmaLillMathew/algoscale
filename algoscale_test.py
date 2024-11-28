import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By


class CreateChromeDriver:

    def __init__(self, languages):
        self.driver = webdriver.Chrome()
        self.languages = languages
        

    def execute_test(self):
        """Opening wikimedia"""
        self.driver.get("https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table")
        tables = self.driver.find_elements(By.TAG_NAME, "table")
        total = 0
        for index, table in enumerate(tables, start=1):
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row_index, row in enumerate(rows, start=1):
                columns = row.find_elements(By.TAG_NAME, "td")
                if len(columns) > 5 and columns[1].text in self.languages:
                    total += int(columns[4].text.replace(',', ''))
        return f"Total articles for {languages}: {total}"


    def run_test(self):
        """
        Start to run test.
        """
        try:
            result = self.execute_test()
            return result
        except Exception as e:
            print(traceback.format_exc())
            print(f"An error occurred: {e}")

        finally:
            # Close the browser
            time.sleep(5)
            self.driver.quit()
            
def findTotalArticlesByLanguages(languages):
    browser = CreateChromeDriver(languages)
    result = browser.run_test()
    return result
    


if __name__ == "__main__":
    
    languages = ["English", "German"]
    total = findTotalArticlesByLanguages(languages)
    print(total)
