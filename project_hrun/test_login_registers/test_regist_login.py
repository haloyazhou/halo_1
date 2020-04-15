import allure
import pytest
@allure.step("注册新账号test1，或已有账户删除再注册")
def step1():
    pass
@allure.step("注册已有账户test1")
def step1_1():
    pass
@allure.step("准备未注册账户")
def step2_1():
    pass
@allure.step("账户不填—填写密码—注册")
def step2_2():
    pass


@allure.step("填写账号和密码正确—登录")
def step3():
    pass
@allure.step("填写账号正确，密码错误—登录")
def step3_1():
    pass
@allure.step("填写账号正确，密码超长—登录")
def step3_2():
    pass
@allure.step("填写账号正确，密码不填—登录")
def step3_3():
    pass
@allure.step("填写密码正确，账号不填—登录")
def step3_4():
    pass

@pytest.mark.hrun
@allure.issue("http://123.56.113.64:9080/api/login/")
@allure.epic("hrun平台接口自动化—登录,注册")
class Test_register_login():
    @allure.feature("注册模块")
    class Test_regist():
        @allure.title("注册账户test1")
        def test_register1(self,xptest_case_register_Delete):
            '''
            用例详情的描述：
                接口地址：http://web.juhe.cn:8080/constellation/getAll
                请求方式：post
                请求类型：Content-Type: application/json
                头信息：
                    X-Requested-With: XMLHttpRequest
                    Content-Type: application/json
                参数：{"account":"test1","email":"1@qq.com","password":"123456","repassword":"123456"}

            大概步骤：
                1.删除账号test1
                2.注册账号test1
            '''
            step1()
            r = xptest_case_register_Delete
            if "恭喜您，账号已成功注册" in r.text:
                print("注册成功")
            assert "恭喜您，账号已成功注册" in r.text
        @allure.title("注册已有账户test1")
        def test_register2(self,xptest_case_register):
            '''
            用例详情的描述：
            接口地址：http://web.juhe.cn:8080/constellation/getAll
            请求方式：post
            请求类型：Content-Type: application/json
            头信息：
                X-Requested-With: XMLHttpRequest
                Content-Type: application/json
            参数：{"account":"test1","email":"1@qq.com","password":"123456","repassword":"123456"}

            大概步骤：
                1.先注册test1
                2.再注册test1
            '''
            step1_1()
            r = xptest_case_register

            # assert "恭喜您，账号已成功注册" in r.text
            if "该用户名已被注册，请更换用户名" in r.text:
                print("账户已注册，请输入新的账号")
            assert "该用户名已被注册，请更换用户名" in r.text

        @allure.title("未注册账户，账户为空")
        def test_register3(self,xptest_case_register):
            '''
            用例详情的描述：
                接口地址：http://web.juhe.cn:8080/constellation/getAll
                请求方式：post
                请求类型：Content-Type: application/json
                头信息：
                    X-Requested-With: XMLHttpRequest
                    Content-Type: application/json
                参数：{"account":"","email":"1@qq.com","password":"123456","repassword":"123456"}

            大概步骤：
                未注册账户，账户不填
            '''
            step2_1()
            step2_2()
            r = xptest_case_register
            if "该用户名已被注册，请更换用户名" in r.text:
                print("请填写账号")
            assert "该用户名已被注册，请更换用户名" in r.text

    @allure.issue("http://123.56.113.64:9080/api/login/")
    @allure.feature("登录模块")
    class Test_login():
        @allure.title("账户，密码正确，登录成功")
        def test_1213(self,login_shili):
            '''
            接口描述：
            接口地址：http://123.56.113.64:9080/api/login/
            请求方式：post
            请求类型：Content-Type: application/x-www-form-urlencoded
            headers头：Content-Type: application/x-www-form-urlencoded
                       Cookie: JSESSIONID.a848f870=node01qe8pjjd6z7jiazrrmss3tntr23.node0
            参数：account=halo&password=123456

            '''
            step3()
            shili=login_shili
            r=shili.login("halo","123456")
            assert "首页" in r.text
            print(r.text)

        @allure.title("密码错误，登录失败")
        def test_2(self,login_shili):
            '''
            接口描述：
                接口地址：http://123.56.113.64:9080/api/login/
                请求方式：post
                请求类型：Content-Type: application/x-www-form-urlencoded
                headers头：Content-Type: application/x-www-form-urlencoded
                           Cookie: JSESSIONID.a848f870=node01qe8pjjd6z7jiazrrmss3tntr23.node0
                参数：account=halo&password=123456

            输入账户密码：
                1.输入正确账户和错误的密码
                2.响应：<title>登录</title>
            '''
            step3_1()
            shili = login_shili
            r=shili.login("halo","23541232")
            assert "登录" in r.text

        @allure.title("密码超长，登录失败")
        def test_3(self,login_shili):
            '''
            接口描述：
                接口地址：http://123.56.113.64:9080/api/login/
                请求方式：post
                请求类型：Content-Type: application/x-www-form-urlencoded
                headers头：Content-Type: application/x-www-form-urlencoded
                           Cookie: JSESSIONID.a848f870=node01qe8pjjd6z7jiazrrmss3tntr23.node0
                参数：account=halo&password=123456

            输入账户密码：
                1.输入正确的密码,账户超长
                2.响应：<title>登录</title>
            '''
            step3_2()
            shili = login_shili
            r=shili.login("halo","asdddddddddasdwqfaf")
            assert "登录" in r.text

        @allure.title("密码不填，登录失败")
        def test_4(self,login_shili):
            '''
            接口描述：
                接口地址：http://123.56.113.64:9080/api/login/
                请求方式：post
                请求类型：Content-Type: application/x-www-form-urlencoded
                headers头：Content-Type: application/x-www-form-urlencoded
                           Cookie: JSESSIONID.a848f870=node01qe8pjjd6z7jiazrrmss3tntr23.node0
                参数：account=halo&password=123456

            输入账户密码：
                1.输入正确的密码,错误的账户
                2.响应：<title>登录</title>
            '''
            step3_3()
            shili = login_shili
            r=shili.login("asev","123456")
            assert "登录" in r.text

        @allure.title("不输入账户，登录失败")
        def test_5(self,login_shili):
            '''
            接口描述：
                接口地址：http://123.56.113.64:9080/api/login/
                请求方式：post
                请求类型：Content-Type: application/x-www-form-urlencoded
                headers头：Content-Type: application/x-www-form-urlencoded
                           Cookie: JSESSIONID.a848f870=node01qe8pjjd6z7jiazrrmss3tntr23.node0
                参数：account=halo&password=123456

            输入账户密码：
                1.输入正确的密码,不输入账户
                2.响应：<title>登录</title>
            '''
            step3_4()
            shili = login_shili
            r=shili.login("","123456")
            print(r.text)
            assert "登录" in r.text







#
# if ""=="":
#     pytest.main(["-s","test_regist_login.py","-m=app"])





