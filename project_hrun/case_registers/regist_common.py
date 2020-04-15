import requests

def case_register(url,user,email):
    s=requests.session()
    body = {
        "account":user,
        "email":email,
        "password":"123456",
        "repassword":"123456"
    }
    header={
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    url=url+"/api/register/"
    # print(os.environ["xadmin_host"])
    r=s.post(url,json=body,headers=header)
    return r

# if ""=="":
#     s=requests.session()
#     url= "http://123.56.113.64:9080/api/register/"
#     data = readyml("register.yml")['register']
#     user=data["user"]
#     email=data["email"]
    # urls=os.environ["xadmin_host"]
#     r=case_register(urls,user,email)
#     print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIII"+ os.environ["xadmin_host"])
