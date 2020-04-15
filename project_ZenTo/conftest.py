import pytest
import requests
from project_ZenTo.login_common.login_r_token_s import login_test
import os
import pytest
from project_ZenTo.register.regist_public import *
#________________________________project_ZenTo
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:9000",
        help="test project_hrun project host address"
    )

@pytest.fixture(scope="session", autouse=True)
def host(request):
    os.environ["xadmin_host"] = request.config.getoption("--cmdhost")

@pytest.fixture
def zhuce_regist():
    '''注册'''
    shili=demo_registe()
    return shili

@pytest.fixture
def login_shili():
    '''登录'''
    shili=login_test()
    return shili


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

