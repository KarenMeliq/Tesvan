import time
import unittest
from selenium import webdriver


class TestInputFields(unittest.TestCase):
    chrome_path = "./chromedriver.exe"
    target_site = 'https://demoqa.com/text-box'

    def test_beforeAll(self):
        self.driver = webdriver.Chrome(self.chrome_path)
        driver = self.driver
        driver.get(self.target_site)

    def test_target_site(self):
        time.sleep(5)
        driver = self.driver
        self.assertIn('ToolsQA', driver.title)

        user_name = "test_user"
        email = "testName@gmail.com"
        current_address = "мои адрес не дом и не улица ..."
        permanent_address = "мои адрес советский союз ... "

        user_name_field = driver.find_element_by_id("userName")
        email_field = driver.find_element_by_id("userEmail")
        current_address_field = driver.find_element_by_id("currentAddress")
        permanent_address_field = driver.find_element_by_id("permanentAddress")
        submit_btn = driver.find_element_by_id("submit")

        time.sleep(3)
        user_name_field.send_keys(user_name)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        time.sleep(1)
        submit_btn.click()
        time.sleep(50)
        self.assertIn("https://demoqa.com/text-box",driver.current_url)

    def afterAll(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
