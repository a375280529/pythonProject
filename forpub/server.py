# -*- coding: utf-8 -*-
#import httplib
import jpype
import os
import time
import sys
from urllib import request
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask,render_template
from flask import request as re
import config
app = Flask(__name__)
app.config.from_object(config)

""" 
传入密钥，加密的税号，进行解密操作
encrypt_key 密钥
nsrsbh_jm 加密的税号
"""

def jiemibibao():
    # 获取执行文件得路径用于更改成exe执行方式后获取文件
    exepath = os.path.realpath(sys.executable)
    endpath = exepath.split(exepath.split("\\")[-1])[0]
    # ①、使用jpype开启虚拟机（在开启jvm之前要加载类路径）
    # exe方式时的jar文件路径获取
    jarpath = os.path.join(os.path.abspath('.'), endpath + "jiajiemi.jar")
    # 加载刚才打包的jar文件
    jarpath = os.path.join(os.path.abspath('.'), 'jiajiemi.jar')
    print(jarpath)

    # 获取jvm.dll的文件路径
    jvmPath = jpype.getDefaultJVMPath()

    # 开启jvm
    jpype.startJVM(jvmPath, '-ea', '-Djava.class.path=%s' % (jarpath))

def end():
    jpype.shutdownJVM()
    time.sleep(1)


def jiemi(encrypt_key,nsrsbh_jiami):
    # 加载java类（参数名是java的长类名）
    javaClass = jpype.JClass('CryptionUtil')

    # 实例化java对象
    javaInstance = javaClass()

    # # 实例化调用方法
    # javaInstance.sh()
    # # 使用类调用静态方法
    # javaClass.show()
    fd = javaClass.decryptNsrsbh(encrypt_key, nsrsbh_jiami)
    return fd

nsrsbh=''
# moco服务的IP端口
moco_ip = '8080'
moco_port = '192.168.86.56'
# 路由服务的IP端口
rout_ser_ip = ''
rout_ser_port = '8000'
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #获取请求URL
        paths = self.path
        #获取headers加密密钥
        encrypt_key = self.headers['encrypt-key']
        # 获取加密的税号
        nsrsbh_jm = (str)(self.path.partition("&")[0]).partition("=")[-1]
        # 对加密税号解密
        nsrsbh = jiemi("sayjyywlpiuwjoro","0s9sef0EVcfD1SDmieqeBzUSCjeWm36J_bU2u0Jg5Ac")
        print(nsrsbh)
        print(123)

        #解密后进行路由到指定税号配置的moco报文
        if paths in "/gateway/anhui?nsrsbh=%s" % nsrsbh:
            try:
                """请求"""
                httpClient = request.Request('http://%s:%s/gateway/anhui?nsrsbh=%s' % (moco_ip,moco_port,nsrsbh))
                """响应"""
                res = request.urlopen(httpClient)
                response = res.read()
                print(response.decode('utf-8'))
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response.decode('utf-8').encode())
            except Exception as e:
                print(e)


# def run():
#     # 默认为127.0.0.1
#     ip = ''
#     port = 8000
#
#     print('starting server,ip, port', ip,port)
#
# # Server settings
#     server_address = (ip, port)
#     httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
#     print('running server...')
#     httpd.serve_forever()


# @app.route("/dd")
# def hello():
#     return render_template("login.html")

@app.route("/gateway/anhui2")
def go():
    print(re.url)
    print(re.args['nsrsbh'])
    return "jjjjjjjj"

@app.route("/gateway/anhui1",methods=['POST'])
def go1():
    print(re.url)
    username = re.json.get("nsrsbh").strip()  # 用户名
    ff = re.headers.get("key").strip()  # key
    print(username)
    print(ff)
    return "ffffff"

@app.route("/gateway/anhui",methods=['POST'])
def go2():
    paths=re.url
    # 获取headers加密密钥
    encrypt_key = re.headers.get("encrypt-key").strip()
    # 获取加密的税号
    nsrsbh = re.json.get("nsrsbh").strip()
    # 对加密税号解密
    nsrsbh = jiemi(encrypt_key, nsrsbh)
    print(nsrsbh)
    paths+="?nsrsbh="+str(nsrsbh)

    #解密后进行路由到指定税号配置的moco报文
    if paths in "/gateway/anhui?nsrsbh=%s" % nsrsbh:
        try:
            """请求"""
            httpClient = request.Request('http://%s:%s/gateway/anhui?nsrsbh=%s' % (moco_ip, moco_port, nsrsbh))
            """响应"""
            res = request.urlopen(httpClient)
            response = res.read()
            print(response.decode('utf-8'))
            # send_response(200)
            # send_header('Content-type', 'application/json')
            # end_headers()
            # wfile.write(response.decode('utf-8').encode())
        except Exception as e:
            print(e)
    return "123"

if __name__ == "__main__":
    try:
        jiemibibao()
        app.run()
    except Exception as e:
        print(e)
    finally:
        end()

# if __name__ == '__main__':
#     try:
#         jiemibibao()
#         run()
#     except Exception as e:
#         print(e)
#     finally:
#         end()
