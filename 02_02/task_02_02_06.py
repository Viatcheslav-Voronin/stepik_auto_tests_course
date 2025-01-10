from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


# Функция вычисления значения для формы
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


def main(url='http://suninjuly.github.io/execute_script.html'):
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Перемещаем окно браузера, так как на мониторе с портретным режимом не работает корректно скролл кнопки
    driver.set_window_position(1500, 0)
    # Разворачиваем окно браузера на весь экран
    driver.maximize_window()
    # Открытие заданной страницы в браузере
    driver.get(url)
    # Получение значения аргумента из текста элемента
    x_value = driver.find_element(By.ID, 'input_value').text
    # Вычисления значения для формы
    result = calc(x_value)
    # Ввод вычисленного значения в поле
    driver.find_element(By.ID, 'answer').send_keys(result)
    # Находим необходимый чек-бокс
    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    # Прокручиваем страницу до чек-бокса
    driver.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    # Отмечаем чек-бокс
    checkbox.click()
    # Находим опцию по ID элемента
    radiobutton = driver.find_element(By.ID, 'robotsRule')
    # Прокручиваем страницу до опции
    driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    # Отмечаем опцию
    radiobutton.click()
    # Находим кнопку отправки данных формы
    button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    # Прокручиваем страницу на нужную высоту
    driver.execute_script('window.scroll(0, 400);')
    # Отправляем данные формы
    button.click()
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

