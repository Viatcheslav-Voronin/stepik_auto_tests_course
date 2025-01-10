from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class TestRegistrationPages(unittest.TestCase):
    def test_registration1(self):
        url = 'http://suninjuly.github.io/registration1.html'
        # Подключение браузера Chrome
        driver = webdriver.Chrome()
        # Открытие заданной страницы в браузере
        driver.get(url)
        # Заполнение полей формы
        driver.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Last name")
        driver.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("First name")
        driver.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("email@site.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("Phone")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Address")
        # Нажимаем кнопку отправки данных формы
        driver.find_element(By.CLASS_NAME, 'btn-default').click()
        # Пауза перед получением результата
        sleep(3)
        # Получение значения текста элемента
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text
        # Пауза перед закрытием браузера
        sleep(10)
        # Закрытие браузера
        driver.quit()
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        url = 'http://suninjuly.github.io/registration2.html'
        # Подключение браузера Chrome
        driver = webdriver.Chrome()
        # Открытие заданной страницы в браузере
        driver.get(url)
        # Заполнение полей формы
        driver.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Last name")
        driver.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("First name")
        driver.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("email@site.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("Phone")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Address")
        # Нажимаем кнопку отправки данных формы
        driver.find_element(By.CLASS_NAME, 'btn-default').click()
        # Пауза перед получением результата
        sleep(3)
        # Получение значения текста элемента
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text
        # Пауза перед закрытием браузера
        sleep(10)
        # Закрытие браузера
        driver.quit()
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)


if __name__ == '__main__':
    unittest.main()

