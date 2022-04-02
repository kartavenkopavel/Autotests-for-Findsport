import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://findsport.dev/"
invalid_phone_list = ["+7 123 999 88 112", "+7 123 999 88", "+7 967 167 99 0", "81231234567а"]
password = "123456"
exp_message_email = "Указана некорректная электронная почта"
exp_message_phone = "Номер телефона должен состоять из 11 цифр, включая код региона. Пример: +7 (901) 123-45-67"
exp_message_phone2 = "Номер телефона не является мобильным."


class TestMainPage():

    @pytest.mark.parametrize('username', invalid_phone_list)
    def test_error_message_for_invalid_phone(self, browser, username):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(3) > a").click()
        browser.find_element(By.ID, "username").send_keys(username)
        browser.find_element(By.ID, "password").send_keys(password)
        browser.find_element(By.ID, "submit").click()
        time.sleep(1)
        act_error_message = browser.find_element(By.CSS_SELECTOR, "#auth-region > div > div.modal__body.l-form > "
                                                                  "div.l-form__row.-js-error-summary.error.summary")

        assert exp_message_phone or exp_message_phone2 or exp_message_email in act_error_message.text
