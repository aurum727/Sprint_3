from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators

class TestExitFromProfil:

    def test_exit_profil_page(self, auth_profile_object):
        """
        Проверка выхода из аккаунта по кнопке «Выйти» в личном кабинете.
        """
        driver = auth_profile_object()
        driver.find_element(*TestLocators.MAIN_PAGE_PROFILE_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.PROFILE_EXIT_KEY)))
        driver.find_element(*TestLocators.PROFILE_EXIT_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.AUTH_LOGIN_BUTTON)))
        assert '/login' in driver.current_url
