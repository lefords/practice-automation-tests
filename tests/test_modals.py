import allure

from pages.modals_page import ModalsPage


@allure.feature("Modals")
class TestModals:

    @allure.title("Открытие простого модального окна")
    def test_simple_modal_opens(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_simple_modal()

        assert page.is_visible(page.SIMPLE_MODAL)


    @allure.title("Проверка текста простого модального окна")
    def test_simple_modal_text(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_simple_modal()

        text = page.get_simple_modal_text()

        assert "simple modal" in text.lower()


    @allure.title("Закрытие простого модального окна")
    def test_simple_modal_closes(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_simple_modal()
        page.close_simple_modal()

        assert page.wait_until_invisible(page.SIMPLE_MODAL)


    @allure.title("Открытие модального окна с формой")
    def test_form_modal_opens(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_form_modal()

        assert page.is_visible(page.FORM_MODAL)


    @allure.title("Поле Name отображается в форме")
    def test_name_field_visible(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_form_modal()

        assert page.is_visible(page.NAME_FIELD)


    @allure.title("Поле Email отображается в форме")
    def test_email_field_visible(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_form_modal()

        assert page.is_visible(page.EMAIL_FIELD)


    @allure.title("Поле Message отображается в форме")
    def test_message_field_visible(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_form_modal()

        assert page.is_visible(page.MESSAGE_FIELD)


    @allure.title("Ввод корректных данных в форму")
    def test_form_accepts_data(self, driver):
        page = ModalsPage(driver)

        page.open_page()
        page.open_form_modal()

        page.enter_name("Alexander")
        page.enter_email("test@example.com")
        page.enter_message("Test message")

        name_value = page.find(
            page.NAME_FIELD
        ).get_attribute("value")

        email_value = page.find(
            page.EMAIL_FIELD
        ).get_attribute("value")

        message_value = page.find(
            page.MESSAGE_FIELD
        ).get_attribute("value")

        assert name_value == "Alexander"
        assert email_value == "test@example.com"
        assert message_value == "Test message"