from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


# Функция вычисления значения для формы
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


def main(url='http://suninjuly.github.io/alert_accept.html'):
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Открытие заданной страницы в браузере
    driver.get(url)
    # Нажимаем на кнопку
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    # Переключаемся на модальное окно предупреждения
    alert = driver.switch_to.alert
    # Нажимаем кнопку "Ок" окна предупреждения
    alert.accept()
    # Получение значения аргумента из текста элемента
    x_value = driver.find_element(By.ID, 'input_value').text
    # Вычисления значения для формы
    result = calc(x_value)
    # Ввод вычисленного значения в поле
    driver.find_element(By.ID, 'answer').send_keys(result)
    # Нажимаем кнопку отправки данных формы
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

