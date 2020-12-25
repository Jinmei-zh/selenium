#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pytest
import json
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Data = [1, 2, 3]

class Test(object):

    @pytest.mark.parametrize("a", Data)
    def test_01(self, a):
        print('测试开始')
        assert a == 2, "信息"


if __name__ == "__main__":
    # 命令行运行 pytest -s -v 3.1.py
    pytest.main(['test01.py', '-sv'])
