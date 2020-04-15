from project_ZenTo.login_common.login_r_token_s import login_test
import requests
import os
class query_infor():
    def __init__(self):
        pass
    def info_query(self):
        url=os.environ["xadmin_host"]+"/api/v1/userinfo"
        shili=login_test()
        shili.login_test_info()
        token=shili.login_token()
        h ={
            "Authorization": "Token %s"%token
        }
        body={
            "name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"
          }
        s=shili.login_s()
        s.headers.update(h)
        r=s.post(url,json=body)
        return r
    def info_query_fail(self):
        url=os.environ["xadmin_host"]+"/api/v1/userinfo"
        shili=login_test()
        shili.login_test_info()
        h ={
            "Authorization": "Token 6d39b7774822cebfe4a382a23e16054c6ecad220"
        }
        body={
            "name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"
          }
        s=shili.login_s()
        s.headers.update(h)
        r=s.post(url,json=body)
        return r

# if ""=="":
#     shili=query_infor()
#     r=shili.info_query()
#     r1=shili.info_query_fail()
#     print(r.text)
#     print(r1.text)