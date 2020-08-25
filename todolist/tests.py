from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
# 단순 HTML 문저 내용의 비교라면 해당함수를 이용할 수 도 있다.
from django.template.loader import render_to_string  
from .views import index  # 아직 만들진 않았지만, 추후에 만들 view함수
# Create your tests here.

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)

        # response = self.client.get('/')
        
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Todo List</title>', html)
        self.assertTrue(html.endswith('</html>'))
        # 아! 호우! 해당 테스트는, mark-up 상태에서의 html과, response로 들어온 html을 비교하는 작업이다.
        # ecpected_html = render_to_string('todolist/index.html')
        # self.assertEqual(html, ecpected_html)
        # 위 두 코드를 합친 것이 아래 코드와 같다.  
        # self.assertTemplateUsed(response, 'todolist/index.html')
        # 일부로 잘못된 template를 가져와보기도 하자.
        # self.assertTemplateNotUsed(response, 'todolist/wrong.html')
