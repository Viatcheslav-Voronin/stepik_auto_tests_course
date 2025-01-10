from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


def main(url='http://suninjuly.github.io/selects1.html'):
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Открытие заданной страницы в браузере
    driver.get(url)
    # Получение значения первого слагаемого
    value1 = driver.find_element(By.ID, 'num1').text
    # Получение значение второго слагаемого
    value2 = driver.find_element(By.ID, 'num2').text
    # Вычисление значения суммы слагаемых
    result = int(value1) + int(value2)
    # Находим элемент с выпадающим списком
    select = Select(driver.find_element(By.ID, 'dropdown'))
    # Выбираем опцию, соответствующую значению найденной суммы
    select.select_by_value(str(result))
    # Нажимаем на кнопку отправки данных формы
    driver.find_element(By.CLASS_NAME, 'btn-default').click()
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

