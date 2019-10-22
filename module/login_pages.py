import unittest
import sys
sys.path.append("../") 
from public.common.read_excel import *  # 从项目路径下导入
from public.common.case_log import log_login_info  # 从项目路径下导入
from public.pages.login import Login


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send(self, case_data):
        username = int(case_data.get('username'))
        password = case_data.get('password')      
        expect_res = case_data.get('expect_res')  # 期望数据

        Login(self.driver).login(username,password)
        time.sleep(1)
        res = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/span').text 
        #log_login_info('test_01',username,password,expect_res,res) 
        self.assertEqual(res, expect_res)  # 断言



if __name__ == "__main__":
    unittest.main()
    print(issubclass(BaseCase,BaseCase))