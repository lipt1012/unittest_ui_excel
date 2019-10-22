# coding=utf-8
import time,datetime
import os.path
from selenium import webdriver
from public.common.logger import Logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# create a logger instance
logger = Logger(logger="BasePage").getlog()

# 封装基本函数 - 执行日志、 异常处理、 截图
class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器并结束测试
    def quit_browser(self):
        self.driver.quit()
        
    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("单击当前页上的“前进”.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("单击当前页上的“后退”.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒." % seconds)

    # 打开网址
    def open_url(self,url):
        self.driver.get(url)
        logger.info("输入 %s 网址." % url)

    # 最大化窗口
    def max_window(self):
        self.driver.maximize_window()
        logger.info("最大化窗口.")

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器.")
        except NameError as e:
            logger.error("退出浏览器失败 %s" % e)

    # 截图
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("截图并保存到文件夹 : /screenshots")
        except NameError as e:
            logger.error("截屏失败! %s" % e)

    # 等待元素可见
    def wait_eleVisible(self,*selector):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(selector))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info('等待元素 {0} 可见，共耗时{1}s '.format(selector, wait_time))
        except:
            logger.info('等待元素 {0} 失败！！！'.format(selector))
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, *selector):
        """
        将其改为传入元组
        传入的时候定义好定位的方式和元素
        """
        try:
            self.wait_eleVisible(*selector)
            element = self.driver.find_element(*selector)
            #logger.info("查找的元素是{0}".format(selector))
            return element
        except NoSuchElementException as e:
            logger.error(" {0} 元素定位异常!!!".format(selector))
            self.get_windows_img()

    # 输入
    def type(self, text, *selector):

        el = self.find_element(*selector)
        el.clear()
        try:
            start = datetime.datetime.now()
            el.send_keys(text)
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info("在元素   {0} 输入 '{1}' 共耗时{2}s ".format(selector,text,wait_time))
        except NameError as e:
            logger.error("无法在元素 {0} 输入".format(selector))
            self.get_windows_img()

    # 清除文本框
    def clear(self, *selector):

        el = self.find_element(*selector)
        try:
            start = datetime.datetime.now()
            el.clear()
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info("清除元素 {0} 内的数据 ,共耗时{1}s ".format(selector,wait_time))
        except NameError as e:
            logger.error("无法清除元素 {0} 内的数据".format(selector))
            self.get_windows_img()

    # 点击元素
    def click(self, *selector):

        el = self.find_element(*selector)
        try:
            start = datetime.datetime.now()
            el.click()
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info("点击元素 {0} ,共耗时{1}s ".format(selector,wait_time))
        except NameError as e:
            logger.error("单击{0}元素失败 ".format(selector))
            self.get_windows_img()

    # 或者网页标题
    def get_page_title(self):
        logger.info("当前页面标题为 %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("等待 %d 秒" % seconds)
    

    #拖动滚动条至底部
    def browser_bottom(self):
        js="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    #拖动滚动条至顶部   
    def browser_top(self):
        js="var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)