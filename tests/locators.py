from selenium.webdriver.common.by import By


class TestLocators:

    REGISTRATION_NAME_FIELD = By.XPATH, '//label[text()="Имя"]/parent::*/input'
    REGISTRATION_LOGIN_FIELD = By.XPATH, '//label[text()="Email"]/parent::*/input'
    REGISTRATION_PASSWORD_FIELD = By.XPATH, '//label[text()="Пароль"]/parent::*/input[@type="password"]'
    REGISTRATION_ENTER_KEY = By.XPATH, '//form/button[text()="Зарегистрироваться"]'

    AUTH_LOGIN_FIELD = By.XPATH, '//div[contains(@class,"input_type_text")]/input[@type="text"]'
    AUTH_PASSWORD_FIELD = By.XPATH, '//div[contains(@class,"input_type_password")]/input[@type="password"]'
    AUTH_LOGIN_BUTTON = By.XPATH, '//form/button[text()="Войти"]'

    UNAUTH_MAIN_PAGE_ENTER_KEY = By.XPATH, '//button[text()="Войти в аккаунт"]'
    UNAUTH_MAIN_PROFILE_ENTER_LINK = By.XPATH, '//header/nav/a[@href="/account"]'
    UNAUTH_REG_RECOVERY_PAGE_ENTER_KEY = By.XPATH, '//a[text()="Войти"]'

    MAIN_PAGE_PROFILE_KEY = By.XPATH, '//p[text()="Личный Кабинет"]'
    PROFILE_PROFILE_LINK = By.XPATH, '//a[text()="Профиль"]'
    PROFILE_EXIT_KEY = By.XPATH, '//button[text()="Выход"]'

    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]'
    LOGO_LINK = By.XPATH, '//div[contains(@class,"AppHeader_header__logo")]/a'

    ACTIVE_BOOKMARK_BRIOCHE = By.XPATH, '//span[text()="Булки"]/parent::*'
    ACTIVE_BOOKMARK_SAUCE = By.XPATH, '//span[text()="Соусы"]/parent::*'
    ACTIVE_BOOKMARK_TOPPINGS = By.XPATH, '//span[text()="Начинки"]/parent::*'

    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'

    INCORRECT_PASSWORD_MESSAGE = By.XPATH, '//p[text()="Некорректный пароль"]'


