from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.ticket = 'STXAgjskckJCvAgarxFdhZRAKlXfbfkCRpt'
        self.driver.get('http://gz-testkyphp.inkept.cn/user/login?ticket=%s' % self.ticket)

    def test_add(self):
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        # 1. 强制等待
        # sleep(1)
        
        # 2. 隐式等待
        # self.driver.implicitly_wait(5)

        # 3. 显示等待
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.presence_of_element_located((By.ID,"gift_id")))
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[2]').click()
        self.driver.find_element_by_id('gift_id[0]').send_keys(110)

if __name__ == '__main__':
    case = TestCase()
    case.test_add()
