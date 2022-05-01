import time
import unittest

from selenium import webdriver


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\chromedriver.exe")

    def test_login_valid_credentials(self):
        driver = self.driver
        driver.get('https://demoqa.com/text-box')
        time.sleep(5)
        self.assertIn("ToolsQA", driver.title)

    user_name = "test_user"
    email = "testName@gmail.com"

    user_name_field = driver.find_element("userName")
    email_field = driver.find_element("userEmail")
    currentAddress_field = driver.find_element("currentAddress")
    permanentAddress_field = driver.find_element("permanentAddress")
    submit_btn = driver.find_element("submit")

    time.sleep(3)
    user_name_field.send_keys(user_name)
    email_field.send_keys(email)
    currentAddress_field.send_keys("test address ...")
    permanentAddress_field.send_keys("test address1 ... ")
    time.sleep(1)
    submit_btn.click()
    time.sleep(2)
    # self.assertIn(" ", driver.current_url)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
