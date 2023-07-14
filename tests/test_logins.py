from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators
from data import Creds

class TestDiffAuth:

    def test_add_new_user(self, driver, auth_profile_object):
        """
        Успешную регистрацию. Поле «Имя» должно быть не пустым;
        в поле Email введён email в формате логин@домен:
        например, 123@ya.ru. Минимальный пароль — шесть символов.

        Проверка регистрации нового пользователя,
        с последующим входом нового пользователя в аккаунт и в профиль.
        """
        driver.get(TestLocators.adres_site+'/register')
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
        driver = auth_profile_object(login=login, password=password, driver_obj=driver)
        driver.find_element(*TestLocators.MAIN_PAGE_PROFILE_KEY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.PROFILE_EXIT_KEY)))
        assert '/account' in driver.current_url

    def test_uncorrect_password(self, auth_profile_object):
        """
        Ошибку для некорректного пароля.
        Проверка, неудачной регистрации.
        При вводе неверного пароля выполняется
        возврат на страницу авторизации
        """
        login = Creds.FALSE_LOGIN
        password = Creds.FALSE_LOGIN
        driver = auth_profile_object(login=login, password=password)
        # проверяем, что после неудачной попытка входа мы остаемся на странице авторизации
        assert '/login' in driver.current_url