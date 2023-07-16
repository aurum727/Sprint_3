from selenium.webdriver.common.by import By


class TestLocators:

    REGISTRATION_NAME_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form[contains(@class,"Auth_form")]/' \
                                        'fieldset[1]/div/div/input'
    REGISTRATION_LOGIN_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form[contains(@class,"Auth_form")]/' \
                                         'fieldset[2]/div/div/input'
    REGISTRATION_PASSWORD_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form[contains(@class,"Auth_form")]/' \
                                            'fieldset[3]/div/div/input[@type="password"]'
    REGISTRATION_ENTER_KEY = By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]'

    AUTH_LOGIN_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/' \
                                 'div[contains(@class,"input_type_text")]/input[@type="text"]'
    AUTH_PASSWORD_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/' \
                                    'div[contains(@class,"input_type_password")]/input[@type="password"]'
    AUTH_LOGIN_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]'

    UNAUTH_MAIN_PAGE_ENTER_KEY = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]'
    UNAUTH_MAIN_PROFILE_ENTER_LINK = By.XPATH, '//*[@id="root"]/div/header/nav/a[@href="/account"]'
    UNAUTH_REG_RECOVERY_PAGE_ENTER_KEY = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a[text()="Войти"]'

    MAIN_PAGE_PROFILE_KEY = By.XPATH, '//*[@id="root"]/div/header/nav/a/p[text()="Личный Кабинет"]'
    PROFILE_PROFILE_LINK = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a[text()="Профиль"]'
    PROFILE_EXIT_KEY = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'

    CONSTRUCTOR_LINK = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p[text()="Конструктор"]'
    LOGO_LINK = By.XPATH, '//*[@id="root"]/div/header/nav/div[contains(@class,"AppHeader_header__logo__")]/a'

    ACTIVE_BOOKMARK_BRIOCHE = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div/span[text()="Булки"]/parent::*'
    ACTIVE_BOOKMARK_SAUCE = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div/span[text()="Соусы"]/parent::*'
    ACTIVE_BOOKMARK_TOPPINGS = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div/span[text()="Начинки"]/parent::*'

    ORDER_BUTTON = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Оформить заказ"]'

    INCORRECT_PASSWORD_MESSAGE = By.XPATH, '//*[@id="root"]/div/main/div/form' \
                                           '/fieldset[2]/div/p[text()="Некорректный пароль"]'



