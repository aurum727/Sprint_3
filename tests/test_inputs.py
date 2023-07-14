from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators

class TestDiffInputs:

    def test_auth_main_page(self, driver):
        """
        вход по кнопке «Войти в аккаунт» на главной
        Проверяем, что при нажатии на кнопку "Войти в аккаунт"
        выполняется переход на страницу авторизации
        """
        # driver = webdriver.Chrome()
        driver.get(TestLocators.adres_site)
        driver.find_element(*TestLocators.UNAUTH_MAIN_PAGE_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        assert '/login' in driver.current_url

    def test_auth_personal_account_page(self, driver):
        """
        вход через кнопку «Личный кабинет»
        Проверяем, переход на страницу авторизации при нажатии на кнопку "Личный кабинет"
        для неавторизованного пользователя
        """
        driver.get(TestLocators.adres_site)
        driver.find_element(*TestLocators.UNAUTH_MAIN_PROFILE_ENTER_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        assert '/login' in driver.current_url

    def test_auth_registration_page(self, driver):
        """
        вход через кнопку в форме регистрации
        Проверяем, переход на страницу авторизации со страницы
        регистрации нового пользователя
        """
        driver.get(TestLocators.adres_site + '/register')
        driver.find_element(*TestLocators.UNAUTH_REG_RECOVERY_PAGE_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        assert '/login' in driver.current_url

    def test_auth_password_recovery_page(self, driver):
        """
        вход через кнопку в форме восстановления пароля
        Проверяем, переход на страницу авторизации со страницы восстановления пароля
        """
        driver.get(TestLocators.adres_site + '/forgot-password')
        driver.find_element(*TestLocators.UNAUTH_REG_RECOVERY_PAGE_ENTER_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_LOGIN_BUTTON)))
        assert '/login' in driver.current_url