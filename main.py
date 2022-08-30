import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys


@pytest.mark.usefixtures('driver2')
class TestLink:
    def test_scenario1(self, driver):
        """
        Verify message submission
        """
        url = "https://www.lambdatest.com/selenium-playground/simple-form-demo"
        driver.get(url)
        msg_text = driver.find_element(By.ID, "user-message")
        in_text = "input text for testing"
        msg_text.send_keys(in_text)
        driver.find_element(By.ID, "showInput").click()

        out_text = driver.find_element(By.ID, "message").text

        assert out_text == in_text

    def test_scenario2(self, driver):
        """
        Verify range success value
        """
        url = "https://www.lambdatest.com/selenium-playground/simple-form-demo"
        driver.get(url)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[1]/div[4]/p').click()
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[1]/div[4]/ul/li[3]/a').click()
        range_success = driver.find_element(By.XPATH, '//*[@id="slider3"]/div/input')
        range_in = 95
        for i in range(range_in-15):
            range_success.send_keys(Keys.RIGHT)
        range_out = driver.find_element(By.ID, "rangeSuccess").text

        assert range_out == str(range_in)

    def test_scenario3(self, driver):
        """
        Verify input form
        """
        url = "https://www.lambdatest.com/selenium-playground/input-form-demo"
        driver.get(url)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[1]/div[1]/ul/li[5]/a').click()
        driver.find_element(By.XPATH, '//*[@id="seleniumform"]/div[6]/button').click()
        assert "Please fill in the fields"

        driver.find_element(By.ID, "name").send_keys('rohit')
        driver.find_element(By.ID, "inputEmail4").send_keys('rohit@binmile.com')
        driver.find_element(By.ID, "inputPassword4").send_keys('rohit')
        driver.find_element(By.ID, "company").send_keys('binmile')
        driver.find_element(By.ID, "websitename").send_keys('binmile.com')
        Select(driver.find_element(By.XPATH, '//*[@id="seleniumform"]/div[3]/div[1]/select')).select_by_visible_text("United States")
        driver.find_element(By.ID, "inputCity").send_keys('noida')
        driver.find_element(By.ID, "inputAddress1").send_keys('inputAddress1')
        driver.find_element(By.ID, "inputAddress2").send_keys('inputAddress2')
        driver.find_element(By.ID, "inputState").send_keys('uttar pradesh')
        driver.find_element(By.ID, "inputZip").send_keys('123456')

        driver.find_element(By.XPATH, '//*[@id="seleniumform"]/div[6]/button').click()
        success_text = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div/p').text

        assert success_text == "Thanks for contacting us, we will get back to you shortly."
