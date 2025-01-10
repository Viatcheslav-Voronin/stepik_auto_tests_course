from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


def main(url='http://suninjuly.github.io/file_input.html'):
    # Абсолютный путь до текущей папки
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Путь до загружаемого файла
    file_path = os.path.join(current_dir, 'file_for_upload.txt')
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Открытие заданной страницы в браузере
    driver.get(url)
    # Заполнение полей формы значениями
    driver.find_element(By.NAME, 'firstname').send_keys("Ivanna")
    driver.find_element(By.NAME, 'lastname').send_keys("Trofimova")
    driver.find_element(By.NAME, 'email').send_keys("Ivanna.Trofimova@internet.ru")
    # Отправка пути файла на форму
    driver.find_element(By.ID, 'file').send_keys(file_path)
    # Находим кнопку отправки данных формы
    button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    # Отправляем данные формы
    button.click()
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

