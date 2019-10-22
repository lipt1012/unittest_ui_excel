import json
import sys
sys.path.append('..')
from config.config import *


def log_login_info(case_name,username,password,expect_res,res):
    logging.info("测试用例：{}".format(case_name))
    logging.info("登录账号：{}".format(username))
    logging.info("登录密码：{}".format(password))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res))

