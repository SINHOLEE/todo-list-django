
## selenium과 geckodriver를 다운받자.
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


# 1 연결하기 전에 테스트 실패하기
# url = 'http://localhost:8000'
# response = requests.get(url)
# html_soup = BeautifulSoup(response.text, 'html.parser')
# title = html_soup.find("title").get_text()

# assert 200 == response.status_code
# assert 'Document' == title

# $ python function_tests.py 
'''
requests.exceptions.ConnectionError: 
HTTPConnectionPool(host='localhost', port=8000): 
Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f62ef23af10>: 
Failed to establish a new connection: [Errno 111] Connection refused'))
'''

# 2. 기능 테스트 통과시키기 
# - 이제 python manage.py를 실행한 다음 다시 테스트를 진행해보자. -> 성공

# 3. 스토리 보드 작성하기

class NewVisitorTest(unittest.TestCase):
    # html_soup:BeautifulSoup = None # 타입을 정의하는게  컨트롤+스페이스바로 함수 찾기 편하다.
    def setUp(self):

        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    # 홈페이지에 방문한 후 제목이 Todo List인 것을 보고 올바른 홈페이지에 방문한 것인지 확인한다.
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 홈페이지 방문
        self.browser.get('http://localhost:8000')

        # 홈페이지의 타이틀이 todo list인지 확인.
        self.assertIn('Todo List', self.browser.title)
        # self.fail()
        
        # h1태그로 감싸져 있는 내용이 '일정목록' 인지 확인
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('일정목록', header_text)


        # 일정을 입력할 수 있는 tag로 바로 이동한다.
        inputbox_with_placeholder = self.browser.find_element_by_id('new-item')
        self.assertEqual('할일을 입력하세요', inputbox_with_placeholder.get_attribute('placeholder'))


        # 사용자는 생일날 미역국을 끓이기 위해 inputbox에 "시장에서 미역 사기"를 입력한다.
        inputbox_with_placeholder.send_keys('시장에서 미역 사기')

        # 사용자가 엔터를 입력하면 페이지를 새로고침해서 모든 일정 목록을 보여준다.
        inputbox_with_placeholder.send_keys(Keys.ENTER)
        time.sleep(1)
        # print(self.browser.get_log())
        # "1: 시장에서 미역 사기"가 첫 번째 할일로 일정 목록에서 보여진다.
        # form 태그를 html 파일에 추가하면, table element를 찾지 못하는 에러가 발생한다. 왜?
        table = self.browser.find_element_by_class_name('todo-list-table')
        # print(self.browser.get_log(log_type='driver'))
        rows = table.find_elements_by_tag_name('tr')
        self.assertEqual('시장에서 미역 사기' ,  rows[0].text if len(rows) else '', 'new to-do item did not appear in table')

        # 사용자는 추가로 할일 텍스트박스에 입력할 수 있고
        self.fail('테스트 종료')
        # "미역을 물에 불리기"라고 입력한다.

        # 다시 페이지를 새로고침해서 입력한 일정 두 가지 모두 목록에 표시한다.

        # 사용자는 일정 목록이 사이트에 올바로 저장되었는지 궁금해서
        # 고유 URL 생성을 확인한다.

        # 사용자는 URL을 방문하고 일정 목록이 올바르게 있음을 확인한다.

        # 사용자는 이제 만족하고 잠을 자러간다.


if __name__ == '__main__':
    unittest.main(warnings='ignore')


## 기능테스트와 단위테스트 차이점

# 단위 테스트    | 기능테스트
# 개발자관점     | 사용자 관점
# 함수단위       | 요구사항 단위
# Mock 사용      | fixture 사용
# 빠름(뭐에대해?) | 느림
# 더 좋은 코드에 기여 | 퇴근에 기여