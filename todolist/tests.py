from django.test import TestCase
# Create your tests here.

# using unittest
# import unittest
import requests
from bs4 import BeautifulSoup


class NewVisitorTest(TestCase):
    def setUp(self):
        url = 'http://localhost:8000'
        response = requests.get(url)
        self.html_soup = BeautifulSoup(response.text, 'html.parser')

    def tearDown(self):
        del self.html_soup

    # 홈페이지에 방문한 후 제목이 Todo List인 것을 보고 올바른 홈페이지에 방문한 것인지 확인한다.
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.assertEqual('Document', self.html_soup.find('title').get_text())
        self.fail()
    
    # 사용자는 생일날 미역국을 끓이기 위해 텍스트박스에 "시장에서 미역 사기"를 입력한다.
    # 사용자가 엔터를 입력하면 페이지를 새로고침해서 모든 일정 목록을 보여준다.
    # "1: 시장에서 미역 사기"가 첫 번째 할일로 일정 목록에서 보여진다.

    # 사용자는 추가로 할일 텍스트박스에 입력할 수 있고
    # "미역을 물에 불리기"라고 입력한다.

    # 다시 페이지를 새로고침해서 입력한 일정 두 가지 모두 목록에 표시한다.

    # 사용자는 일정 목록이 사이트에 올바로 저장되었는지 궁금해서
    # 고유 URL 생성을 확인한다.

    # 사용자는 URL을 방문하고 일정 목록이 올바르게 있음을 확인한다.

    # 사용자는 이제 만족하고 잠을 자러간다.

