from random import randrange


class Creds:

    TRUE_NAME = "au_rum_11_727@gmail.com"
    TRUE_PASSWORD = "26122008"

    FAKE_NAME = f"Яндекс_{randrange(10, 99)}"
    FAKE_LOGIN = f"pavel_zolotov_11_{randrange(100, 999)}@gmail.com"
    FAKE_PASSWORD = randrange(100000, 999999)

    FALSE_LOGIN = "pavel_zolotov_11_727@gmail.com"
    FALSE_PASSWORD = "123"
