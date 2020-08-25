from django.test import TestCase
# Create your tests here.

# using unittest
# import unittest
import requests
from bs4 import BeautifulSoup


class SmokeTest(TestCase):
    # 일부로 자명하게 틀린 테스트를 실행하므로써 test 준비동작을 마무리한다..? 왜 일부로 자명한 테스트를 하는거지? 철학이 궁금하다.
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)