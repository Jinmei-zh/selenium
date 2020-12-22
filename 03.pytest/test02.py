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
def get_conf():
    with open('./test.json') as f:
        params = json.load(f)
        return params

class TestCase(object):
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        # 登陆验证
        self.ticket = 'STXAgjskckJCvAgarxFdhZRAKlXfbfkCRpt'
        self.driver.get('http://gz-testkyphp.inkept.cn/user/login?ticket=%s' % self.ticket)
        self.vars = {}
    
    def teardown_method(self, method):
      self.driver.quit()

    @pytest.mark.parametrize("data", get_conf())
    def test_add(self, data):
        print('打泡泡全局设置测试-%s' % data['name'])
        # print(data['message'])
        
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        # 等待添加按钮节点出现
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID,"gift_id")))

        # 点击添加按钮
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[2]').click()
        
        # 当data.value有值时赋值
        if data['value']:
            sleep(1)
            # 选择礼物id为1
            gift_id = self.driver.find_elements_by_id('gift_id[0]')
            gift_id[0].click()
            gift_id[1].send_keys(data['value'])

            sleep(1)
            gift_id[1].send_keys(Keys.TAB)

        # 点击提交
        sleep(1)
        btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]')
        btn.click()

        # 获取提示信息 ant-message-error
        sleep(1)
        if self.driver.find_elements_by_class_name('ant-form-explain'):
            error = self.driver.find_elements_by_class_name('ant-form-explain')[0]
        else :
            error = self.driver.find_element_by_css_selector('.ant-message-custom-content>span')
        error_msg = error.get_attribute('innerHTML')
        assert error_msg == data['message'], '错误'

if __name__ == "__main__":
    pytest.main(['test02.py', '-sv'])
    pass