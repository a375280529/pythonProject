#!/usr/bin/python
# -*- coding: utf-8 -*-
import paramiko
import time
import os

if __name__ == '__main__':
    # 创建SSHClient实例对象
    ssh = paramiko.SSHClient()

    # 调用方法，标识没有远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接远程机器 地址端口用户名密码
    ssh.connect("192.168.81.71", 22, "root", "centos")

    #前几天就传几
    lastdaynum=12
    nowday = time.strftime("%Y%m%d", time.localtime(time.time()-86400*lastdaynum))
    # 执行命令
    #stdin, stdout, stderr = ssh.exec_command("cd feedbacklist; mkdir ceshi ;cd ceshi;touch aa.txt;mv aa.txt bb.txt;ls")

    stdin, stdout, stderr = ssh.exec_command("cd feedbacklist; mkdir ceshi ;cd ceshi;touch aa.txt;mv aa.txt aa"+nowday+".txt;ls")

    # 获取命令结果
    result = stdout.read()
    print(str(result, encoding='utf-8'))
    # ssh.exec_command("mkdir ces")
    # ssh.exec_command("cd ces")
    # stdin, stdout, stderr = ssh.exec_command("pwd")

    #获取Transport实例
    tran = ssh.get_transport()
    # 获取sftp实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 设置上传的本地和远程文件路径
    localpath = "aa.txt"
    removepath = os.path.join('/root/feedbacklist/ceshi/', 'cc.txt')
    # 执行上传动作
    sftp.put(localpath, removepath)

    localpath = "templates/templates.txt"
    removepath=os.path.join('/root/feedbacklist/ceshi/', 'aa20210930.txt')
    sftp.get(removepath,localpath)

    # 关闭连接
    sftp.close()
    tran.close()
    ssh.close()
