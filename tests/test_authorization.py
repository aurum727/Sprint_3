from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators
from data import Creds
from urls import AdressSite

class TestAutorization:

    def test_auth_main_page(self, driver, auth_profile_object):
        """
        вход по кнопке «Войти в аккаунт» на главной
        Проверяем, что при нажатии на кнопку "Войти в аккаунт"
        выполняется переход на страницу авторизации
        """
        driver.get(AdressSite.main_page)
        driver.find_element(*TestLocators.UNAUTH_MAIN_PAGE_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        driver.find_element(*TestLocators.AUTH_LOGIN_FIELD).send_keys(Creds.TRUE_NAME)
        driver.find_element(*TestLocators.AUTH_PASSWORD_FIELD).send_keys(Creds.TRUE_PASSWORD)
        driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_auth_personal_account_page(self, driver, auth_profile_object):
        """
        вход через кнопку «Личный кабинет»
        Проверяем, переход на страницу авторизации при нажатии на кнопку "Личный кабинет"
        для неавторизованного пользователя
        """
        driver.get(AdressSite.main_page)
        driver.find_element(*TestLocators.UNAUTH_MAIN_PROFILE_ENTER_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        driver.find_element(*TestLocators.AUTH_LOGIN_FIELD).send_keys(Creds.TRUE_NAME)
        driver.find_element(*TestLocators.AUTH_PASSWORD_FIELD).send_keys(Creds.TRUE_PASSWORD)
        driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_auth_registration_page(self, driver, auth_profile_object):
        """
        вход через кнопку в форме регистрации
        Проверяем, переход на страницу авторизации со страницы
        регистрации нового пользователя
        """
        driver.get(AdressSite.register_page)
        driver.find_element(*TestLocators.UNAUTH_REG_RECOVERY_PAGE_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        driver.find_element(*TestLocators.AUTH_LOGIN_FIELD).send_keys(Creds.TRUE_NAME)
        driver.find_element(*TestLocators.AUTH_PASSWORD_FIELD).send_keys(Creds.TRUE_PASSWORD)
        driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_auth_password_recovery_page(self, driver, auth_profile_object):
        """
        вход через кнопку в форме восстановления пароля
        Проверяем, переход на страницу авторизации со страницы восстановления пароля
        """
        driver.get(AdressSite.password_recovery_page)
        driver.find_element(*TestLocators.UNAUTH_REG_RECOVERY_PAGE_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        driver.find_element(*TestLocators.AUTH_LOGIN_FIELD).send_keys(Creds.TRUE_NAME)
        driver.find_element(*TestLocators.AUTH_PASSWORD_FIELD).send_keys(Creds.TRUE_PASSWORD)
        driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)