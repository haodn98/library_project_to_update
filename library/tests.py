from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class AuthTest(TestCase):

    VALID_CREDENTIALS = {
        'email': 'testadmin@gmail.com',
        'password': 'Test123!'
    }
    INVALID_CREDENTIALS = {
        'email': 'wrongtestadmin@gmail.com',
        'password': 'wrongTest123!'
    }

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_valid_data(self):
        url = 'http://127.0.0.1:8000/'
        self.driver.get(url=url)
        self.driver.find_element(By.ID, "login").click()
        time.sleep(2)

        email_form = self.driver.find_element(By.NAME, "email")
        password_form = self.driver.find_element(By.NAME, "password")

        email_form.clear()
        email_form.send_keys(self.VALID_CREDENTIALS["email"])

        password_form.clear()
        password_form.send_keys(self.VALID_CREDENTIALS["password"])

        self.driver.find_element(By.ID, "login_button").click()

        self.assertEqual("Home page", self.driver.title)
        time.sleep(3)

        self.driver.find_element(By.ID, 'logout').click()
        self.assertEqual("Login page", self.driver.title)
        time.sleep(1)
        self.driver.quit()

    def test_invalid_data(self):
        url = 'http://127.0.0.1:8000/'
        self.driver.get(url=url)
        self.driver.find_element(By.ID,"login").click()
        time.sleep(2)
        email_form = self.driver.find_element(By.NAME, "email")
        password_form = self.driver.find_element(By.NAME, "password")

        email_form.clear()
        email_form.send_keys(self.INVALID_CREDENTIALS["email"])

        password_form.clear()
        password_form.send_keys(self.INVALID_CREDENTIALS["password"])
        time.sleep(2)
        self.driver.find_element(By.ID, "login_button").click()

        error = self.driver.find_element(By.XPATH, "//*[text()='Incorrect Login or Password']")
        self.assertTrue(error.is_displayed())
        self.assertEqual("Incorrect Login or Password", error.text)
        self.assertEqual("Login page", self.driver.title)
        time.sleep(1)
        self.driver.quit()

    def tearDown(self) -> None:
        pass