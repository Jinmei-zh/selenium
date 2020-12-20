from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        self.driver.get('http://www.baidu.com')
        sleep(1)
        # id定位
        self.driver.find_element_by_id('kw').send_keys('element')
        # xpath定位
        # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('element')
        sleep(1)
        self.driver.find_element_by_id('su').click()

        sleep(3)
        self.driver.quit()

    def test_move(self):
        self.driver.get('http://www.baidu.com')
        sleep(1)

        action = ActionChains(self.driver)
        el = self.driver.find_element_by_xpath('//*[@id="s-top-left"]/div/a')
        action.move_to_element(el).perform()

        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_search()
    # case.test_move()