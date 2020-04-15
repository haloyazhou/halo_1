import allure
from project_ZenTo.infomation.information_query import query_infor
from project_ZenTo.modify_inform.modify import modify_test
import pytest

@allure.step("注册账户test")
def step1d():
    pass
@allure.step("输入已注册账号test")
def step2d():
    pass

@allure.step("准备未注册账户")
def step1_1re():
    pass
@allure.step("准备已注册账户")
def step1_2re():
    pass
@allure.step("注册")
def step2re():
    pass

@allure.step("成功登陆")
def step1ck():
    pass
@allure.step("查询个人信息，传正确token")
def step2ck():
    pass
@allure.step("查询个人信息，传错误token")
def step3ck():
    pass

@allure.step("登陆")
def step1xg():
    pass
@allure.step("sex类型传M")
def step2_1xg():
    pass
@allure.step("sex类型传F")
def step2_2xg():
    pass
@allure.step("sex类型传X")
def step2_3xg():
    pass
@allure.step("sex类型为空")
def step3xg():
    pass
@allure.step("修改信息传参：通过性验证")
def step2_1_1xg():
    pass
@allure.step("传参name=test1")
def step2_1_2xg():
    pass

@pytest.mark.ZenTo
@allure.epic("halo_项目")
class Test_halo():

    @allure.feature("注册")
    class Test_regist():
        @allure.title(" 注册-用一个没注册过的账号注册，注册成功")
        def test_success(self,zhuce_regist):
            '''
            前置条件
                账号没注册过，或者在user表中已删除

            用例步骤：
                访问地址/api/v1/register

                headers :
                    Content-Type: application/json
                body:
                    {
                    "username": "test",
                    "password": "123456",
                   "mail": "1233@qq.com"}

            预期：
                {'code': 0, 'msg': '注册成功!'}

            '''
            step1_1re()
            step2re()
            shili=zhuce_regist
            r=shili.register_test112()
            shili.success()
            # print(r.text)
            assert r.json()["code"]==2000

        @allure.title(" 注册-用一个已注册过的账号注册，提示：用户已被注册")
        def test_fail(self,zhuce_regist):
            '''
            前置条件
                用户已注册过（user表已存在），如test

            用例步骤：
                访问地址/api/v1/register

                headers :
                    Content-Type: application/json
                body:
                    {
                    "username": "test",
                    "password": "123456",
                   "mail": "1233@qq.com"}

            预期：
                {'code': 2000, 'msg': 'test用户已被注册'}

            '''
            step1_2re()
            step2re()
            shili=zhuce_regist
            r=shili.register_test112()
            shili.success0()
            print(r.text)
            assert r.json()["code"]==2000

    @allure.issue("http://49.235.92.12:8080/zentao/testcase-browse-3--byModule-16.html")
    @allure.feature("登录")
    class Test_mokuai():
        @allure.story("未注册，已注册登录")
        class Test_aaome():
            @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-30-1.html")
            @allure.title("注册test账户-登陆接口-输入正确账号,正确密码，登陆成功")
            def test_No_regist_success(self,login_shili):
                '''
                前置条件
                    1.已注册过的账号信息，如：
                        username test
                        password 123456
                        访问地址：/api/v1/login

                必填参数：
                    body:
                    {
                    "username": "test",
                    "password": "123456"
                    }

                预期结果：
                    {"code": 0, "msg": "login success!", "username": "test1", "token": "c0b60d1589cb322d293982ebbc48351d3d0ce11f"}
                '''
                # shi=demo_registe()
                # shi.register_test112()
                # shi.success()
                step1d()
                step2d()
                shili=login_shili
                r=shili.login_test_info()
                print("结果输出：%s"%r.text)
                print(r.text)
                assert r.json()["code"]==0

            @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-31-1.html")
            @allure.title("登陆接口-输入一个未注册的账号，登陆失败")
            # @allure.story(" 登陆接口-输入一个未注册的账号，登陆失败")
            def test_success(self,login_shili):
                '''
                前置条件
                    1.已注册过的账号，如：
                        username test
                        password 123456
                        访问地址：/api/v1/login

                必填参数：
                    body:
                    {
                    "username": "xxxyyy",
                    "password": "123456"
                    }

                预期结果：
                    {"code": 3003, "msg": "\u8d26\u53f7\u6216\u5bc6\u7801\u4e0d\u6b63\u786e", "username": "xxxyyy", "token": ""}
                '''
                step1d()
                step2d()
                shili=login_shili
                r=shili.login_test_info("xxxyyy","123456")
                print("结果输出：%s"%r.text)
                assert r.json()["code"]==3003
        @allure.story("参数组合")
        class Test_login_fail():
            @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-463-1.html")
            @allure.title("必填参数，密码不填")
            def test_fail(self,login_shili):
                '''
                前置条件
                    1.已注册过的账号，如：
                        username test
                        password 123456
                        访问地址：/api/v1/login

                必填参数
                    body:
                    {
                    "username": "test",
                    "password": ""
                    }

                预期结果：
                    {"code": 3113, "msg": "请输入密码", "username": "test", "token": ""}
                '''
                step2d()
                shili=login_shili
                r=shili.login_test_info()
                print('结果输出：{"code": 3113, "msg": "请输入密码", "username": "test", "token": ""}')

    @allure.feature("查看个人信息")
    @allure.issue("http://49.235.92.12:8080/zentao/testcase-browse-3--byModule-18.html")
    class Test_mokuai1():
        @allure.title("修改成功案例")
        @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-34-1.html")
        def test_infomation_success(self):
            '''
            前置条件
                1.已注册过的账号，如：
                    username test
                    password 123456
                    访问地址：/api/v1/userinfo

            获取最新头部，例：
                Authorization: Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx

            必填参数：
                body={
                    "name": "test",
                    "sex": "M",
                    "age": 20,
                    "mail": "283340479@qq.com"
                  }

            预期结果：
                {"msg":"sucess!","code":0,"data":[{"id":105,"name":"test","sex":"M","age":20,"mail":"283340479@qq.com","create_time":"2019-12-28"}]}
            '''
            step1ck()
            step2ck()
            shili=query_infor()
            r=shili.info_query()
            print(r.text)
            assert r.json()["message"] == "update some data!"




        @allure.issue("http://49.235.92.12:8080/zentao/testcase-browse-3--byModule-18.html")
        @allure.story("必填参数，不填或错误的参数")
        class Test_infoma_fail():

            @allure.title("查询接口-传错误的token，不能获取到个人信息")
            @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-34-1.html")
            def test_infomation_success(self):
                '''
                前置条件
                    1.已注册过的账号，如：
                        username test
                        password 123456
                        访问地址：/api/v1/userinfo

                错误的请求头部：
                    Authorization: Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx

                必填参数：
                    body={
                        "name": "test",
                        "sex": "M",
                        "age": 20,
                        "mail": "283340479@qq.com"
                      }

                预期结果：
                    {"detail":"Invalid token."}
                '''
                step1ck()
                step3ck()
                shili=query_infor()
                r=shili.info_query_fail()
                print(r.text)
                assert r.json()["detail"] == "Invalid token."

    @allure.issue("http://49.235.92.12:8080/zentao/testcase-browse-3--byModule-17.html ")
    @allure.feature("修改个人信息")
    class Test_modify_inform_test():
        @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-32-1.html")
        @allure.title("修改个人信息-修改自己的个人信息，修改成功")
        def test_modify_success0(self,login_shili):
            '''
            前置条件
                1.用户已经登陆
                2.name参数是当前用户的登陆用户

            步骤:
                POST http://49.235.92.12:9000/api/v1/userinfo HTTP/1.1

                Authorization: Token 6965a529fedca8cc89c8ec70b884c378045da82c
                Content-Type: application/json
                {"name": "test", "sex": "M", "age": 20, "mail": "283340479@qq.com"}

            预期结果：
                {"message":"update some data!","code":0,"data":{"name":"test","sex":"M","age":20,"mail":"283340479@qq.com"}}
            :param login_shili:
            :return:
            '''
            step1xg()
            step2_1_1xg()

            shili=login_shili
            shili.login_test_info()
            s=shili.login_s()
            token=shili.login_token()

            shili1=modify_test(s,token)
            r=shili1.modify_test_info()
            print(r.text)
            assert r.json()["message"]=="update some data!"
            print(r.text)
            print(r.text)

        @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-33-1.html")
        @allure.title("修改个人信息-修改不是本人的用户信息，无权限操作")
        def test_modify_success(self,login_shili):
            '''
            前置条件
                1.用户已登陆，如：test
                2.name参数与登陆用户参数不一致，如test2
            步骤:
                POST http://49.235.92.12:9000/api/v1/userinfo HTTP/1.1

                Authorization: Token 6965a529fedca8cc89c8ec70b884c378045da82c
                Content-Type: application/json
                {"name": "test", "sex": "M", "age": 20, "mail": "283340479@qq.com"}
            预期结果：
                {"message":"无权限操作","code":4000,"data":[]}
            :param login_shili:
            :return:
            '''
            step1xg()
            step2_1_2xg()

            shili=login_shili
            shili.login_test_info()
            s=shili.login_s()
            token=shili.login_token()

            shili1=modify_test(s,token)
            r=shili1.modify_test_info("test1")
            print(r.text)
            assert r.json()["message"]=="无权限操作"

        @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-297-2.html")
        @allure.story("修改个人信息-sex参数传F,M和空类型，成功(枚举类型) ")
        class Test_F_M_type():
            @allure.title("修改个人信息-sex参数传M")
            def test_modify_success1(self,login_shili):
                '''
                前置条件
                    1.用户已登陆，如：test
                    2.name参数与登陆用户参数不一致，如test2
                步骤:
                    POST http://49.235.92.12:9000/api/v1/userinfo HTTP/1.1

                    Authorization: Token 6965a529fedca8cc89c8ec70b884c378045da82c
                    Content-Type: application/json
                    {"name": "test", "sex": "M", "age": 20, "mail": "283340479@qq.com"}

                预期结果：
                    {"message":"无权限操作","code":4000,"data":[]}
                :param login_shili:
                :return:
                '''
                step1xg()
                step2_1xg()

                shili=login_shili
                shili.login_test_info()
                s=shili.login_s()
                token=shili.login_token()

                shili1=modify_test(s,token)
                r=shili1.modify_test_info()
                print(r.text)
                assert r.json()["message"]=="update some data!"

            @allure.title("修改个人信息-sex参数传F")
            def test_modify_sueccss2(self,login_shili):
                '''
                前置条件
                    1.用户已登陆，如：test
                    2.name参数是当前用户的登陆用户
                步骤:
                    POST http://49.235.92.12:9000/api/v1/userinfo HTTP/1.1

                    Authorization: Token 6965a529fedca8cc89c8ec70b884c378045da82c
                    Content-Type: application/json
                    {"name": "test", "sex": "F", "age": 20, "mail": "283340479@qq.com"}

                预期结果：
                    {"message":"update some data!","code":3333,"data":[]}
                :param login_shili:
                :return:
                '''
                step1xg()
                step2_2xg()
                shili=login_shili
                shili.login_test_info()
                s=shili.login_s()
                token=shili.login_token()

                shili1=modify_test(s,token)
                r=shili1.modify_test_info("test","F")
                print(r.text)
                assert r.json()["message"]=="update some data!"

            @allure.title("修改个人信息-sex参数传X")
            def test_modify_fail(self,login_shili):
                '''
                前置条件
                    1.用户已登陆，如：test
                    2.name参数是当前用户的登陆用户
                步骤:
                    POST http://49.235.92.12:9000/api/v1/userinfo HTTP/1.1

                    Authorization: Token 6965a529fedca8cc89c8ec70b884c378045da82c
                    Content-Type: application/json
                    {"name": "test", "sex": "X", "age": 20, "mail": "283340479@qq.com"}

                预期结果：
                    {"message":"参数类型错误","code":3333,"data":[]}
                :param login_shili:
                :return:
                '''
                step1xg()
                step2_3xg()
                shili=login_shili
                shili.login_test_info()
                s=shili.login_s()
                token=shili.login_token()

                shili1=modify_test(s,token)
                r=shili1.modify_test_info("test","X")
                print(r.text)
                assert r.json()["message"]=="参数类型错误"

            @allure.title("修改个人信息-sex参数为空")
            def test_modify_sueccss3(self,login_shili):
                '''
                前置条件
                    1.用户已登陆，如：test
                    2.name参数是当前用户的登陆用户
                步骤:
                    POST http://49.235.92.12:9000/api/v1/userinfo HTTP/1.1

                    Authorization: Token 6965a529fedca8cc89c8ec70b884c378045da82c
                    Content-Type: application/json
                    {"name": "test", "sex": "", "age": 20, "mail": "283340479@qq.com"}

                预期结果：
                    {"message":"update some data!","code":0,"data":{"name":"test","sex":"","age":20,"mail":"283340479@qq.com"}}
                :param login_shili:
                :return:
                '''
                step1xg()
                step3xg()

                shili=login_shili
                shili.login_test_info()
                s=shili.login_s()
                token=shili.login_token()

                shili1=modify_test(s,token)
                r=shili1.modify_test_info("test","")
                print(r.text)
                assert r.json()["data"]["sex"]==""



