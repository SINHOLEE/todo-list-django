from django.test import TestCase
from django.urls import resolve
from .views import index  # 아직 만들진 않았지만, 추후에 만들 view함수
# Create your tests here.

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    