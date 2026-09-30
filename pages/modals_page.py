import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ModalsPage(BasePage):
    URL = "https://practice-automation.com/modals/"

    SIMPLE_MODAL_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Simple Modal')]"
    )

    FORM_MODAL_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Form Modal')]"
    )

    SIMPLE_MODAL = (
        By.ID,
        "popmake-1318"
    )

    SIMPLE_MODAL_TEXT = (
        By.XPATH,
        "//div[@id='popmake-1318']//p"
    )

    SIMPLE_MODAL_CLOSE = (
        By.XPATH,
        "//div[@id='popmake-1318']//button[contains(@class, 'pum-close')]"
    )

    FORM_MODAL = (
        By.ID,
        "popmake-674"
    )

    FORM_MODAL_CLOSE = (
        By.XPATH,
        "//div[@id='popmake-674']//button[contains(@class, 'pum-close')]"
    )

    NAME_FIELD = (
        By.ID,
        "g1051-name"
    )

    EMAIL_FIELD = (
        By.ID,
        "g1051-email"
    )

    MESSAGE_FIELD = (
        By.ID,
        "contact-form-comment-g1051-message"
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        "//div[@id='popmake-674']//button[@type='submit']"
    )

    @allure.step("Открыть страницу Modals")
    def open_page(self):
        self.open(self.URL)

    @allure.step("Открыть простое модальное окно")
    def open_simple_modal(self):
        self.click(self.SIMPLE_MODAL_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(
                self.SIMPLE_MODAL
            )
        )

    @allure.step("Получить текст простого модального окна")
    def get_simple_modal_text(self):
        return self.get_text(self.SIMPLE_MODAL_TEXT)

    @allure.step("Закрыть простое модальное окно")
    def close_simple_modal(self):
        self.click(self.SIMPLE_MODAL_CLOSE)

    @allure.step("Открыть модальное окно с формой")
    def open_form_modal(self):
        self.click(self.FORM_MODAL_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(
                self.FORM_MODAL
            )
        )

    @allure.step("Закрыть модальное окно с формой")
    def close_form_modal(self):
        self.click(self.FORM_MODAL_CLOSE)

    @allure.step("Заполнить имя: {name}")
    def enter_name(self, name):
        self.type_text(self.NAME_FIELD, name)

    @allure.step("Заполнить email: {email}")
    def enter_email(self, email):
        self.type_text(self.EMAIL_FIELD, email)

    @allure.step("Заполнить сообщение")
    def enter_message(self, message):
        self.type_text(self.MESSAGE_FIELD, message)