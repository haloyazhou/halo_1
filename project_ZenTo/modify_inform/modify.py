import os

class modify_test():
    def __init__(self,s,token):
        self.s=s
        self.token=token
    def modify_test_info(self,name="test",sex="M"):
        url=os.environ["xadmin_host"]+"/api/v1/userinfo"
        body={
            "name": name,
            "sex": sex,
            "age": 20,
            "mail": "283340479@qq.com"
        }
        h={
            "Authorization": "Token %s"%self.token
        }
        self.s.headers.update(h)
        r=self.s.post(url,json=body)
        return r