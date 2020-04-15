import yaml
import os
yaml.warnings({'YAMLLoadWarning': False})

def readyml(yamlPath):
    curPath = os.path.dirname(os.path.realpath(__file__))
    yamPath = os.path.join(curPath,yamlPath)
    if not os.path.isfile(yamPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamPath)

    f = open(yamPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg)
    return d

# if __name__ == '__main__':
#     # data = readyml()
#     # "register.yml"['register']
#     data= readyml('register.yml')['register']
#     # data1=list(data)
#     print(data['pwd'])
#     # print(data['pwd'])




#
#
# yaml安装：
# 文件说明：
#    lxml-4.4.3-cp36-cp36m-win_amd64.whl          yaml文件
#       python36 匹配 lxml4.4.3
# 下载地址
#      https://www.lfd.uci.edu/~gohlke/pythonlibs/
# 安装操作：进入下载的文件-cmd-输入(需要pip设置环境变量)
#      pip install lxml-4.4.3-cp36-cp36m-win_amd64.whll
# (没有wheel库需要：pip install wheel）