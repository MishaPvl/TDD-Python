from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import unittest

# Параметр executable_path больше не используется в текущей версии selenium`a, 
# теперь вместо него нужно передавать экземпляр класса Service:

class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''установка'''
        s = Service('\.venv\Scripts\geckodriver.exe')
        self.browser = webdriver.Firefox(service=s)

    def test_can_start_a_list_and_retrieve_it_later(self):
    # В браузере открывется страница сайта
        self.browser.get('http://localhost:8000')

    # В заголовке сайта написано 'To-Do'
    assert 'To-Do' in browser.title

# Предлагается ввести элемент списка

# Набрать в текстовом поле произвольный текст 

# После нажатия клавиши Enter страница обновляется и теперь содержит: '1. Введённый текст'

# В текстовое поле по прежнему можно добавить новый элемент

# После ввода нового элемента страница снова обновляется, и теперь показывает оба элемента из списка

# Сайт генерирует уникальный URl для каждого пользователя 

browser.quit()