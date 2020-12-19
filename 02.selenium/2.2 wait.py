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

    def test_search(self):
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        sleep(1)
        self.driver.find_element_by_id('gift_id').send_keys('111')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[1]').click()

        sleep(3)
        self.driver.quit()

    def test_add(self):
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.presence_of_element_located((By.ID,"gift_id")))
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[2]').click()
        #  self.driver.find_element_by_id('gift_id[0]').send_keys(110)

if __name__ == '__main__':
    case = TestCase()
    # case.test_search()
    case.test_add()
