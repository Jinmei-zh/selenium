from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.ticket = 'STXAgjskckJCvAgarxFdhZRAKlXfbfkCRpt'
        # 登陆验证
        self.driver.get('http://gz-testkyphp.inkept.cn/user/login?ticket=%s' % self.ticket)

    def test_search(self):
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        sleep(1)
        # 搜索礼物Id = 111的礼物
        self.driver.find_element_by_id('gift_id').send_keys('111')

        sleep(1)
        # 点击搜索
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[1]').click()

        sleep(1)
        el = self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/div/div/div/div/div/div/div/table/tbody/tr/td[2]')
        gift_id = el.get_attribute('innerHTML')
        if gift_id == '111':
            print('测试通过')
        else:
            print('测试失败%s' % gift_id)

        sleep(1)
        self.driver.quit()

    def test_add_error(self):
        print('不选择礼物id提示测试：')
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        # 等待添加按钮节点出现
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID,"gift_id")))

        # 点击添加按钮
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[2]').click()
        
        # 点击提交
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()

        # 获取错误提示信息
        error = self.driver.find_elements_by_class_name('ant-form-explain')[0]
        error_msg = error.get_attribute('innerHTML')
        if error_msg == '请选择礼物id':
            print('测试通过')
        else:
            print('测试失败%s' % error_msg)
        sleep(1)
        self.driver.quit()

    def test_add_isexist(self):
        print('已存在礼物id测试：')
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)

        # 等待添加按钮节点出现
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID,"gift_id")))

        # 点击添加按钮
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[2]').click()
        
        sleep(1)
        # 选择礼物id为1
        gift_id = self.driver.find_elements_by_id('gift_id[0]')
        gift_id[0].click()
        gift_id[1].send_keys(1)

        sleep(1)
        gift_id[1].send_keys(Keys.TAB)

        # 点击提交
        sleep(1)
        btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]')
        btn.click()

        # 获取提示信息 ant-message-error
        sleep(1)
        error = self.driver.find_element_by_css_selector('.ant-message-error>span')
        error_msg = error.get_attribute('innerHTML')
        if error_msg == '礼物id{1}已存在':
            print('测试通过')
        else:
            print('测试失败%s' % error_msg)
        
        sleep(1)
        self.driver.quit()
      
    def test_add_success(self):
        print('添加礼物成功测试：')
        self.driver.get('http://gz-testky.inkept.cn/pao-pao-config/list?ticket=%s' % self.ticket)
        # 等待添加按钮节点出现
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID,"gift_id")))

        # 点击添加按钮
        self.driver.find_element_by_xpath('//*[@id="entry-container"]/section/section/main/div/section/form/div[3]/button[2]').click()
        
        sleep(1)
        # 选择礼物id
        gift_id = self.driver.find_elements_by_id('gift_id[0]')
        gift_id[0].click()
        gift_id[1].send_keys(119) # 选择礼物id为21

        sleep(1)
        gift_id[1].send_keys(Keys.TAB)

        # 点击提交
        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]')
        btn.click()

        # 获取提示信息 ant-message
        sleep(1)
        error = self.driver.find_element_by_css_selector('.ant-message-custom-content>span')
        error_msg = error.get_attribute('innerHTML')
        if error_msg == '提交成功':
            print('测试通过')
        else:
            print('测试失败%s' % error_msg)
        
        sleep(1)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_search()
    # case.test_add_error()
    # case.test_add_isexist()
    # case.test_add_success()
