from selenium import webdriver
import pytest

link = "https://findsport.dev/"
login = "9671679902"
password = "123456"
exp_error_empty = "Пожалуйста, введите e-mail или телефон, пароль"


@pytest.fixture()
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


class TestMainPage():

    def test_auth_verified_phone(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#header > section > div > div:nth-child(3) > a").click()
        browser.find_element_by_id("username").send_keys(login)
        browser.find_element_by_id("password").send_keys(password)
        browser.find_element_by_id("submit").click()


    def test_empty_form(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#header > section > div > div:nth-child(3) > a").click()
        browser.find_element_by_id("submit").click()
        error_notification = browser.find_element_by_css_selector("#auth-region > div > div.modal__body.l-form > "
                                                                  "div.l-form__row.-js-error-summary.error.summary")
        act_error_empty = error_notification.text
        if act_error_empty == exp_error_empty:
            print("\nCorrect notification")
        else:
            print("\nInvalid notification")
