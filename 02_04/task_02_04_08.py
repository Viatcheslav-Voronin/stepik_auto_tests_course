from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import log, sin


# Функция вычисления значения для формы
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


def main(url='http://suninjuly.github.io/explicit_wait2.html'):
    # Подключение браузера Chrome
    driver = webdriver.Chrome()
    # Открытие заданной страницы в браузере
    driver.get(url)
    # Ждем не более 12 секунд пока текст элемента не будет равен заданному значению
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    #  Нажимаем кнопку заказа
    driver.find_element(By.ID, 'book').click()
    # Получение значения аргумента из текста элемента
    x_value = driver.find_element(By.ID, 'input_value').text
    # Вычисления значения для формы
    result = calc(x_value)
    # Ввод вычисленного значения в поле
    driver.find_element(By.ID, 'answer').send_keys(result)
    # Нажимаем кнопку отправки данных формы
    driver.find_element(By.ID, 'solve').click()
    # Пауза перед закрытием браузера
    sleep(10)
    # Закрытие браузера
    driver.quit()


if __name__ == '__main__':
    main()

