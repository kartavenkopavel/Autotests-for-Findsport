import time

from selenium import webdriver
import pytest

link = "https://findsport.dev/"
exp_placeholder_text = "E-mail или телефон"
exp_placeholder_text2 = "Введите e-mail или телефон"


@pytest.fixture()
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


class TestMainPage():
    def test_ui_placeholder_empty(self, browser):
        browser.get(link)
        act_placeholder = browser.find_element_by_id("username")
        act_placeholder_text = act_placeholder.get_attribute("placeholder")
        if act_placeholder_text == exp_placeholder_text:
            print("\nThe text matches")
        else:
            print(f"\nThe text doesn't matches. Actual result: {act_placeholder_text}")



