from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators
from data import AdressSite

class TestProfile:

    def test_auth_and_enter_profile(self, auth_profile_object):
        """
        Проверка перехода в настройки пользователя (страница профиля)
        по клику на «Личный кабинет».
        """
        driver = auth_profile_object()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.MAIN_PAGE_PROFILE_KEY)))

        driver.find_element(*TestLocators.MAIN_PAGE_PROFILE_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE_PROFILE_LINK)))
        assert '/account/profile' in driver.current_url

    def test_move_from_profile_constructor_click(self, auth_profile_object):
        """
        Проверь переход из Личного кабинета по клику на ссылку «Конструктор».
        Загрузка главной страницы
        """
        driver = auth_profile_object()
        driver.find_element(*TestLocators.MAIN_PAGE_PROFILE_KEY).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_LINK).click()
        assert AdressSite.main_page in driver.current_url

    def test_move_from_profile_logo_click(self, auth_profile_object):
        """
        Проверка перехода из Личного кабинета по клику
        на ссылку с логотипом Stellar Burgers.
        Загрузка главной страницы
        """
        driver = auth_profile_object()
        driver.find_element(*TestLocators.MAIN_PAGE_PROFILE_KEY).click()
        driver.find_element(*TestLocators.LOGO_LINK).click()
        assert AdressSite.main_page in driver.current_url