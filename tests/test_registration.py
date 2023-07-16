from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators
from data import Creds
from urls import AdressSite


class TestRegistration:

    def test_add_new_user(self, driver, auth_profile_object):
        """
        Успешную регистрацию. Поле «Имя» должно быть не пустым;
        в поле Email введён email в формате логин@домен:
        например, 123@ya.ru. Минимальный пароль — шесть символов.

        Проверка регистрации нового пользователя,
        с ожиданием перехода на страницу авторизации,
        авторизация нового пользователяи переход на
        главную страницу с появлением кнопки "Оформить заказ"
        """
        driver.get(AdressSite.register_page)
        name = Creds.FAKE_NAME
        login = Creds.FAKE_LOGIN
        password = Creds.FAKE_PASSWORD
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(name)
        driver.find_element(*TestLocators.REGISTRATION_LOGIN_FIELD).send_keys(login)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))

        driver.find_element(*TestLocators.AUTH_LOGIN_FIELD).send_keys(login)
        driver.find_element(*TestLocators.AUTH_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.ORDER_BUTTON)))

        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_incorrect_password(self, driver):
        """
        Ошибку для некорректного пароля длиной три символа,
        вместо допустимых 6-ти символов.
        Проверяем формат длины пароля при регистрации нового пользователя.
        """
        driver.get(AdressSite.register_page)
        name = Creds.TRUE_NAME
        login = Creds.FALSE_LOGIN
        password = Creds.FALSE_PASSWORD
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(name)
        driver.find_element(*TestLocators.REGISTRATION_LOGIN_FIELD).send_keys(login)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_ENTER_KEY).click()

        WebDriverWait(driver, 5).\
            until(expected_conditions.element_to_be_clickable((TestLocators.INCORRECT_PASSWORD_MESSAGE)))

        assert driver.find_element(*TestLocators.INCORRECT_PASSWORD_MESSAGE)