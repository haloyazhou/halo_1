import requests
import os


class login_test():
    def __init__(self):
        self.s=requests.session()
        self.token=""


    def login_test_info(self,user="test",pwd="123456"):
        url=os.environ["xadmin_host"]+"/api/v1/login"
        body={
            "username":user ,
            "password": pwd
        }

        self.r=self.s.post(url,json=body)
        if self.r.json()["msg"]=="login success!" :
            print("登录成功")
        self.token= self.r.json()["token"]
        return self.r

    def login_s(self):
        return self.s
    def login_token(self):
        return self.token

# if ""=="":
#     # def test_aaa(zhuce_regist):
#     #     pass
#     shili=login_test()
#     # shili.aaa()
#     r=shili.login_test_info()
#     print(r.text)
#     print(shili.login_token())