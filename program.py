"Metrics Assignment"
import unittest
import json
from selenium import webdriver



class Tester(unittest.TestCase):
    "Class For Test"

    def setUp(self):
        "doc string"
        self.driver = webdriver.Chrome(r"C:\Users\tushar\Desktop\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verification_errors = []

    def test_project(self):
        "Function for getting performace"

        driver = self.driver
        total_values = {}


        with open("output.txt", "w") as json_file:
            for result in range(10):
                driver.get("https://en.wikipedia.org/wiki/Software_metric")
                result = driver.execute_script("return window.performance.getEntries()")


                for current in result:
                    url = current["name"]
                    current_list = total_values.get(url, [])
                    current_list.append(current["duration"])
                    total_values[url] = current_list
                    json_file.write(f"{current['name']}, {current['duration']}\n")



        with open("excel_file.csv", "w") as csv_file:
            for key, value in total_values.items():
                average_duration = sum(value) / len(total_values)
                csv_file.write(f"{key}, {average_duration}\n")



        with open("json_file" + ".json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verification_errors)


if __name__ == "__main__":
    unittest.main()
