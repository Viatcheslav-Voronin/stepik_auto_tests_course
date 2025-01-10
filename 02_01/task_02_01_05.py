from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


# Функция вычисления значения для формы
def calc(x):
  return str(log(abs(12*sin(int(x)))))


def main(url='https://suninjuly.github.io/math.html'):
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Открытие заданной страницы в браузере
    driver.get(url)
    # Получение значения аргумента из атрибута элемента
    x_value = driver.find_element(By.ID, 'input_value').text
    # Вычисления значения для формы
    y_value = calc(x_value)
    # Ввод вычисленного значения в поле
    driver.find_element(By.ID, 'answer').send_keys(y_value)
    # Проставляем необходимый чек-бокс
    driver.find_element(By.ID, 'robotCheckbox').click()
    # Выбираем нужную опцию
    driver.find_element(By.ID, 'robotsRule').click()
    # Нажимаем на кнопку отправки данных формы
    driver.find_element(By.CLASS_NAME, 'btn-default').click()
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

