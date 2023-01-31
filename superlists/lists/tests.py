from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        # Мы проверяем, чтобы resolve, когда ее вызывают с «/», то есть корнем сайта, 
        # нашла функцию под названием home_page
        self.assertEqual(found.func, home_page)
