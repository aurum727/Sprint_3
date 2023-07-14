from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators


class TestConstructor:

    def test_brioche(self, auth_profile_object):
        """
        Проверка, работы перехода к разделам: Булки
        как критерий - смотрим появление у элемента переключения закладок "Булки"
        класса содержащего tab_tab_type_current__
        """
        driver = auth_profile_object()
        WebDriverWait(driver, 5). \
            until(expected_conditions.visibility_of_element_located((TestLocators.ACTIVE_BOOKMARK_BRIOCHE)))

        is_active_class = driver.find_element(*TestLocators.ACTIVE_BOOKMARK_BRIOCHE).get_attribute('class')
        if 'tab_tab_type_current__' not in is_active_class:
            driver.find_element(*TestLocators.ACTIVE_BOOKMARK_BRIOCHE).click()
            is_active_class = driver.find_element(*TestLocators.ACTIVE_BOOKMARK_BRIOCHE).get_attribute('class')

        assert 'tab_tab_type_current__' in is_active_class

    def test_sauce(self, auth_profile_object):
        """
        Проверить, что работают переходы к разделам: Соусы
        как критерий - смотрим появление у элемента переключения закладок "Соусы"
        класса содержащего tab_tab_type_current__
        """
        driver = auth_profile_object()
        WebDriverWait(driver, 5). \
            until(expected_conditions.visibility_of_element_located((TestLocators.ACTIVE_BOOKMARK_SAUCE)))

        is_active_class = driver.find_element(*TestLocators.ACTIVE_BOOKMARK_SAUCE).get_attribute('class')
        if 'tab_tab_type_current__' not in is_active_class:
            driver.find_element(*TestLocators.ACTIVE_BOOKMARK_SAUCE).click()
            is_active_class = driver.find_element(*TestLocators.ACTIVE_BOOKMARK_SAUCE).get_attribute('class')

        assert 'tab_tab_type_current__' in is_active_class

    def test_topping(self, auth_profile_object):
        """
        Проверка, что работает переход к разделу Начинки
        как критерий - смотрим появление у элемента переключения закладок "Начинки"
        класса содержащего tab_tab_type_current__
        """
        driver = auth_profile_object()
        WebDriverWait(driver, 5). \
            until(expected_conditions.visibility_of_element_located((TestLocators.ACTIVE_BOOKMARK_TOPPINGS)))

        is_active_class = driver.find_element(*TestLocators.ACTIVE_BOOKMARK_TOPPINGS).get_attribute('class')
        if 'tab_tab_type_current__' not in is_active_class:
            driver.find_element(*TestLocators.ACTIVE_BOOKMARK_TOPPINGS).click()
            is_active_class = driver.find_element(*TestLocators.ACTIVE_BOOKMARK_TOPPINGS).get_attribute('class')

        assert 'tab_tab_type_current__' in is_active_class