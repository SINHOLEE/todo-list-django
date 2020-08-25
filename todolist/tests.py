from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import index  # 아직 만들진 않았지만, 추후에 만들 view함수
# Create your tests here.

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Todo List</title>', html)
        self.assertTrue(html.endswith('</html>'))