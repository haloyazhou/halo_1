import requests
import allure
import os
class demo_registe():

    def __init__(self):
        pass
    def register_test112(self,user="test",name="123456",mail="1233@qq.com"):
        url = os.environ["xadmin_host"] +"/api/v1/register"
        body={
            "username": user,
            "password": name,
            "mail": mail
        }
        r=requests.post(url,json=body)
        # print(r.text)
        self.r=r
        return r
    def success(self):
        if "2000" in self.r.text:
            print("{'code': 0, 'msg': '账户test注册成功!'}")
    def success0(self):
        if "2000" in self.r.text:
            print("{'code': 2000, 'msg': 'test用户已被注册'}")

# if ""=="":
    # shili=demo_registe()
    # r=shili.register_test112()
    # print(r.text)
