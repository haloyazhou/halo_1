import pytest
from common_mysql.connect_mysql import*
from common_yml.read_yml import readyml
from project_hrun.case_login.login import login_1
from project_hrun.case_registers.regist_common import case_register
import os
#________________________________project_hrun
@pytest.fixture
def xptest_case_register():
    '''注册已有账户'''
    data = readyml("register.yml")['register']
    user=data["user"]
    email=data["email"]
    urls=os.environ["xadmin_host"]
    r=case_register(urls,user,email)
    return r
@pytest.fixture
def xptest_case_register_Delete():
    '''注册新账号'''
    os.environ["xadmin_host"] ="http://123.56.113.64:9080"
    execute_sql('DELETE from UserInfo WHERE username="test1"')
    data = readyml("register.yml")['register']
    user=data["user"]
    email=data["email"]
    urls=os.environ["xadmin_host"]
    r=case_register(urls,user,email)
    return r

@pytest.fixture
def login_shili():
    '''登录'''
    shili = login_1()
    return shili



# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdhost",#定义名称
#         action="store",
#         default="http://123.56.113.64:9080",
#         help="test project_hrun project host address"
#     )
# @pytest.fixture(scope="session", autouse=True)
# def host(request):
#     os.environ["xadmin_host"] = request.config.getoption("--cmdhost")















# '''
# pytest --alluredir ./report/allure_raw
#
# pytest --alluredir ./report/allure_raw --allure-epics=epic
#
# allure serve report/allure_raw
#
#
# allure对用例的等级划分成五个等级
#  blocker　 阻塞缺陷（功能未实现，无法下一步）
#  critical　　严重缺陷（功能点缺失）
#  normal　　 一般缺陷（边界情况，格式错误）
#  minor　 次要缺陷（界面错误与ui需求不符）
#  trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
#
# '''

# def pytest_addoption(parser):
#     parser.adoption(
#         "--cmddhost",#定义名称
#         action="store",
#         default="http://49.235.92.12:8020",
#         help="test project_hrun project host address"
#     )
#
# @pytest.fixture(scope="session", autouse=True)
# def host(request):
#     os.environ["xadmin_host"] = request.config.getoption("--cmdhost")
