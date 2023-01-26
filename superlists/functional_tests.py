from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Параметр executable_path больше не используется в текущей версии selenium`a, 
# теперь вместо него нужно передавать экземпляр класса Service:

s = Service('\.venv\Scripts\geckodriver.exe')
browser = webdriver.Firefox(service=s)
browser.get('http://localhost:8000')

assert 'The install worked successfully! Congratulations!' in browser.title