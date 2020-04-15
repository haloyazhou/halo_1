import os
class login_case1():
    def __init__(self,s):
        self.s=s
    def login_test(self,user="test",pwd="123456"):
        url=os.environ["xadmin_host"]+"/api/v1/login"
        body={
            "username":user ,
            "password": pwd
        }

        r=self.s.post(url,json=body)
        return r

# if ""=="":
#     s=requests.session()
#     shili=login_case1(s)
#     r=shili.login_test()
#     token=r.json()["token"]
#     print(token)
#     print(r.text)