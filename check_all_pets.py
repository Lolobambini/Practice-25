from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # неявные ожидания
implicitly_waits = driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody')  # неявные ожидания


def test_show_my_pets():
    # Вводим email
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))  # явные ожидания
    pytest.driver.find_element_by_id('email').send_keys('40222505@mail.ru')
    # Вводим пароль
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    pytest.driver.find_element_by_id('pass').send_keys('123')
    # Нажимаем на кнопку входа в аккаунт
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Мои питомцы")]')))
    pytest.driver.find_element_by_xpath('//a[contains(text(), "Мои питомцы")]').click()
    # Проверяем, что мы оказались на главной странице пользователя

    assert pytest.driver.current_url == 'http://petfriends1.herokuapp.com/my_pets'


    pytest.driver.quit()


def test_my_pets():
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


@pytest.fixture(autouse=True)
def testing(driver=True):
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

def click():
    pass

    descriptions = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody')
    images = pytest.driver.find_elements_by_xpath('//*[id="all_my_pets"]//img')
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//body/tr/td[0]')
    statistics = pytest.driver.find_elements_by_xpath('//div[@class=".col-sm-4 left"]/text[1]')
    f = filter(str.isdecimal, statistics)
    statistics_2 = "".join(f)  # оставляем только число из текста

    for i in range(len(names)):
        assert statistics_2 == len(descriptions)  # Присутствуют все питомцы
        assert statistics_2 == len(images)  # Хотя бы у половины питомцев есть фото
        assert statistics_2 == len(names)  # У всех питомцев есть имя, возраст и порода

animals_names = ['laki', 'jopka']
unique = []


def test_get_unique_names():  # У всех питомцев разные имена
    for animals_names in unique:
        if animals_names in unique:
            continue
        else:
            unique.append(animals_names)
        return unique


print(test_get_unique_names())
