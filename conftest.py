import pytest
# импортировали пакет Selenium WebDriver
from selenium import webdriver
from tests.locators import TestLocators
from tests.data import Creds

@pytest.fixture
def driver(scope='function'):
    """
    Фикстура для создания инстанса драйвера, передаем его в функцию,
    возвращаем инстанс и закрываем драйвер
    """
    driver = webdriver.Chrome()
    # driver.get(TestLocators.adres_site)
    yield driver
    driver.quit()


@pytest.fixture
def auth_profile_object(driver):
    """
    фикстура для авторизации на сайте
    может принимать параметры логин, пароль и объект драйвера
    по умолчанию верные логин и пароль
    Функция выполняет авторизацию на сайте и ожидает появления элемента для перехода в Личный кабинет
    """
    def _auth_profile_object(login=Creds.TRUE_NAME, password=Creds.TRUE_PASSWORD, driver_obj=driver):
        driver = driver_obj
        driver.get(TestLocators.adres_site + '/login')
        driver.find_element(*TestLocators.AUTH_LOGIN_FIELD).send_keys(login)
        driver.find_element(*TestLocators.AUTH_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
        return driver
    return _auth_profile_object
