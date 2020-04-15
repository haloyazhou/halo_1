import requests
import os


class login_1():
    def __init__(self):
        pass
    def login(self,user='halo',pwd='123456'):
        s=requests.session()
        body = {
            "account":user,
            "password":pwd
        }

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        url="http://123.56.113.64:9080/api/login/"
        # url=os.environ["xadmin_host"]+"/api/login/"
        r=s.post(url,data=body,headers=header)

        return r

# if ""=="":
#     shili = login_1()
#     d=shili.login()
#     print(d.text)