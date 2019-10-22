import logging
import os
import time
from optparse import OptionParser

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'case')   # 用例目录
today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report_{}.html'.format(now))  # 更改路径到report目录下
#log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
#report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下
data_file = os.path.join(prj_path, 'data', 'test_user_data.xlsx')
# log配置
# logging.basicConfig(level=logging.INFO,  # log level
#                     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
#                     datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
#                     filename=log_file,  # 日志输出文件
#                     filemode='a')  # 追加模式

url = '***'

# 数据库配置
db_host = '***'
db_port = 3306
db_user = 'test'
db_passwd = '***'
db = 'api_test'

send_email_after_run = False
# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '***'
smtp_password = '***'

sender = smtp_user  # 发件人
receiver = '***'  # 收件人
subject = 'UI测试报告'  # 邮件主题
