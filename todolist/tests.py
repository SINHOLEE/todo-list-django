from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
# 단순 HTML 문저 내용의 비교라면 해당함수를 이용할 수 도 있다.
from django.template.loader import render_to_string  
from .views import index  # 아직 만들진 않았지만, 추후에 만들 view함수
from .models import Todo
# Create your tests here.

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        response = self.client.get('/')
        
        # 아! 호우! 해당 테스트는, mark-up 상태에서의 html과, response로 들어온 html을 비교하는 작업이다.
        # ecpected_html = render_to_string('todolist/index.html')
        # self.assertEqual(html, ecpected_html)
        # 위 두 코드를 합친 것이 아래 코드와 같다.  
        self.assertTemplateUsed(response, 'todolist/index.html')
        # 일부로 잘못된 template를 가져와보기도 하자.
        self.assertTemplateNotUsed(response, 'todolist/wrong.html')

    # def test_index_page_after_post_returns_correct_html(self): 내가 지은 이름
    def test_index_page_can_save_a_post_request(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['content'] = '시장에서 미역 사기'

        # response = index(request)

        data = {'content': '시장에서 미역 사기'}
        response = self.client.post('/', data=data)
        # print(response.content.decode())
        self.assertIn('시장에서 미역 사기', response.content.decode())
        data = {'content': '집가서 미역국 끓이기'}
        response = self.client.post('/', data=data)
        # print(response.content.decode())
        self.assertIn('집가서 미역국 끓이기', response.content.decode())
        # self.assertEqual( response.context.todo_list[0].content, '시장에서 미역 사기')

    def test_index_page_can_delete_a_table_item(self):
        data = {'content': '시장에서 미역 사기'}
        response = self.client.post('/', data=data)
        
        data = {'content': '집가서 미역국 끓이기'}
        response = self.client.post('/', data=data)
        
        response = self.client.post('/delete/1') # ok 상태만 출력

        response = self.client.get('/')
        print(response.content.decode())
        self.assertNotIn('시장에서 미역 사기', response.content.decode())

class TodoModelTest(TestCase):
    def test_read_todo_model_with_empty_db(self):
        
        self.assertEqual(Todo.objects.exists(), False)
    
    def test_create_todo_model_with_empty_db(self):
        todo = Todo()
        todo.content  = '시장에서 미역 사기'
        todo.save()
        self.assertEqual(todo.content, '시장에서 미역 사기')
        self.assertEqual(todo.pk, 1)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.is_completed, False)

    def test_delete_todo_model_with_a_todo(self):
        # create first
        todo = Todo()
        todo.content  = '시장에서 미역 사기'
        todo.save()
        self.assertTrue(Todo.objects.exists())
        self.assertEqual(Todo.objects.get(pk=1).content, '시장에서 미역 사기')
        
        # 빈 공간에서 새로 만들었으니, pk는 1
        # 여러번 시도하면 pk값은 autoincrement이니 당연히 pk값이 증가하게 되면서 테스트가 틀려야 할 것 같은데 그렇지 않는다.
        todo = Todo.objects.get(pk=1)
        todo.delete()

        self.assertEqual(Todo.objects.exists(), False)        