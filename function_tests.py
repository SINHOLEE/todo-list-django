'''
## selenium과 geckodriver를 다운받자.
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


binary = '/usr/lib/firefox'
options = Options()
options.set_headless(headless=True)
options.binary = binary


cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

browser = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="/usr/bin/geckodrivber")


browser = webdriver.Firefox()
browser.get('http://google.com')

# assert 'Django' in browser.title
print(browser.title)

# selenium은 ubuntu cli 환경에서 동작하지 않는것같다..... 실패!
'''


import requests
from bs4 import BeautifulSoup

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

# 사용자는 todolist 홈페이지에 접속한다.
url = 'http://localhost:8000'
response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
title = html_soup.find("title").get_text()

# 홈페이지에 방문한 후 제목이 Todo List인 것을 보고 올바른 홈페이지에 방문한 것인지 확인한다.
assert 'Todo List' == title, 'title was '+ title 

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
