from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


def main(url='http://suninjuly.github.io/cats.html'):
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Открытие заданной страницы в браузере
    driver.get(url)
    try:
        # Поиск элемента на странице
        driver.find_element(By.ID, 'button')
    except NoSuchElementException as e:
        # Обработка исключения в случае, если элемент не найден на странице
        print('NoSuchElementException')
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

