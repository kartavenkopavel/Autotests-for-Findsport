from selenium.webdriver.common.by import By

link = "https://findsport.dev/"
exp_placeholder_text = "E-mail или телефон"
exp_placeholder_text2 = "Введите e-mail или телефон"


class TestMainPage():
    def test_ui_placeholder_empty(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(3) > a").click()
        act_placeholder = browser.find_element(By.ID, "username")
        act_placeholder_text = act_placeholder.get_attribute("placeholder")
        if act_placeholder_text == exp_placeholder_text:
            print("\nThe text matches")
        else:
            print(f"\nThe text doesn't matches. Actual result: {act_placeholder_text}")

    def test_ui_placeholder_tap(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#header > section > div > div:nth-child(3) > a").click()
        browser.find_element(By.ID, "username").click()
        act_placeholder = browser.find_element(By.ID, "username")
        act_placeholder_text = act_placeholder.get_attribute("placeholder")
        if act_placeholder_text == exp_placeholder_text2:
            print("\nThe text matches")
        else:
            print(f"\nThe text doesn't matches. Actual result: {act_placeholder_text}")
