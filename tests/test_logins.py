import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators
from data import Creds, AdressSite

class TestDiffAuth:

    def test_add_new_user(self, driver, auth_profile_object):
        """
        Успешную регистрацию. Поле «Имя» должно быть не пустым;
        в поле Email введён email в формате логин@домен:
        например, 123@ya.ru. Минимальный пароль — шесть символов.

        Проверка регистрации нового пользователя,
        с ожиданием перехода на страницу авторизации.
        """
        driver.get(AdressSite.register_page)
        # генерируем случайные данные для регистрации нового пользователя в соответствии с шаблоном
        name = Creds.FAKE_NAME
        login = Creds.FAKE_LOGIN
        password = Creds.FAKE_PASSWORD
        # заполняем поля формы регистрации соответствующими данными и жмем кнопку подтвержения регистрации
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(name)
        driver.find_element(*TestLocators.REGISTRATION_LOGIN_FIELD).send_keys(login)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        assert '/login' in driver.current_url

    def test_incorrect_password(self, auth_profile_object):
        """
        Ошибку для некорректного пароля.
        Проверка, неудачной регистрации.
        При вводе неверного пароля
        проверяем, что происходит возврат на страницу авторизации ("/login").
        появление сообщения о неверном пароле не выводится в Chromium Driver
        (в отличии например от Yandex browser, где такое сообщение появляется..)
        """
        login = Creds.FALSE_LOGIN
        password = Creds.FALSE_PASSWORD
        driver = auth_profile_object(login=login, password=password)
        assert '/login' in driver.current_url