from selenium.webdriver.common.by import By
import time

link = "https://findsport.dev/"
login = "9671679902"
unverified_login = "+79231234567"
password = "123456"
exp_login = "test2 master"
exp_error_empty = "Пожалуйста, введите e-mail или телефон, пароль"
exp_error_not_found = "С указанным телефоном не зарегистрирован ни один пользователь"


class TestMainPage():

    def test_auth_verified_phone(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(3) > a").click()
        browser.find_element(By.ID, "username").send_keys(login)
        browser.find_element(By.ID, "password").send_keys(password)
        browser.find_element(By.ID, "submit").click()
        time.sleep(1)
        username = browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(2) > div > a")
        act_login = username.text
        if act_login == exp_login:
            print("\nAuthorization success")
        else:
            print("\nAuthorization failed")

    def test_empty_form(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(3) > a").click()
        browser.find_element(By.ID, "submit").click()
        error_notification = browser.find_element(By.CSS_SELECTOR, "#auth-region > div > div.modal__body.l-form > "
                                                                   "div.l-form__row.-js-error-summary.error.summary")
        act_error_empty = error_notification.text
        if act_error_empty == exp_error_empty:
            print("\nCorrect notification")
        else:
            print("\nInvalid notification")

    def test_auth_unverified_phone(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(3) > a").click()
        browser.find_element(By.ID, "username").send_keys(unverified_login)
        browser.find_element(By.ID, "password").send_keys(password)
        browser.find_element(By.ID, "submit").click()
        time.sleep(1)
        error_notification = browser.find_element(By.CSS_SELECTOR, "#auth-region > div > div.modal__body.l-form > "
                                                                   "div.l-form__row.-js-error-summary.error.summary")
        act_error_not_found = error_notification.text
        if act_error_not_found == exp_error_not_found:
            print("\nCorrect notification")
        else:
            print(f"\nInvalid notification: {act_error_not_found}")
