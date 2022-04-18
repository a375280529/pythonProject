#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import os
import sys
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import zipfile
import configparser


# 获取配置文件相对路径
def getIniPath():
    # path = os.path.dirname(os.path.abspath(__file__))
    # path = path.split(path.split('\\')[-1])[0] + "iniFile" + "\\"
    exepath = os.path.realpath(sys.executable)
    endpath = exepath.split(exepath.split("\\")[-1])[0]
    path = os.path.join(os.path.abspath('.'), endpath + "iniFile\\")
    return path

# 读取配置文件的方法，ini为配置文件名称
def readini(ini):
    path = getIniPath() + ini
    config = configparser.ConfigParser()
    config.read(path,encoding="utf-8-sig")
    return config

#读取ini配置文件数据
def getIni(ini):
    config = readini(ini)
    return config

def zip_by_volume(file_path, block_size):
  """zip文件分卷压缩"""
  file_size = os.path.getsize(file_path) # 文件字节数
  path, file_name = os.path.split(file_path) # 除去文件名以外的path，文件名
  suffix = file_name.split('.')[-1] # 文件后缀名
  # 添加到临时压缩文件
  zip_file = file_path + '.zip'
  with zipfile.ZipFile(zip_file, 'w') as zf:
    zf.write(file_path, arcname=file_name)
  # 小于分卷尺寸则直接返回压缩文件路径
  if file_size <= block_size:
    return zip_file
  else:
    fp = open(zip_file, 'rb')
    count = file_size // block_size + 1
    # 创建分卷压缩文件的保存路径
    save_dir = path + os.sep + file_name + '_split'
    if os.path.exists(save_dir):
      from shutil import rmtree
      rmtree(save_dir)
    os.mkdir(save_dir)
    # 拆分压缩包为分卷文件
    for i in range(1, count + 1):
      _suffix = 'zip.'+'0{:0>2}'.format(i)
      name = save_dir + os.sep + file_name.replace(str(suffix), _suffix)
      f = open(name, 'wb+')
      if i == 1:
        f.write(b'\x50\x4b\x07\x08') # 添加分卷压缩header(4字节)
        f.write(fp.read(block_size - 4))
      else:
        f.write(fp.read(block_size))
    fp.close()
    os.remove(zip_file)   # 删除临时的 zip 文件
    return save_dir

def send_mail(onepath,fujianname,index,mail_host,mail_user,mail_pass,sender,receive,ms,header,subject):
    receivers = receive.split(";")

    # 邮件正文是MIMEText
    msg = MIMEText(ms, 'html', 'utf-8')
    # 邮件对象
    message = MIMEMultipart()
    message['From'] = Header(header+index, 'utf-8')
    message['To']=";".join(receivers)
    message['date']=time.strftime("%a,%d %b %Y %H:%M:%S %z")

    subject = subject+index
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(msg)

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(onepath, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    #附件名称可以为中文
    att1.add_header("Content-Disposition", "attachment", filename=("utf-8", "", fujianname))
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("第"+index+"个邮件发送成功。。。")
    except smtplib.SMTPException as e:
        print("error", e)
        print("except: 第"+index+"个邮件无法发送。。。")

if __name__ == '__main__':
    ini = getIni("sendmailslogger.ini")
    emailmsg=ini["emailmsg"]
    mail_host=emailmsg["mailhost"]
    mail_user = emailmsg["mailuser"]
    mail_pass = emailmsg["mailpass"]
    sender=emailmsg["sender"]
    receive=emailmsg["receive"]
    header=emailmsg["header"]
    subject=emailmsg["subject"]
    msg=emailmsg["msg"]
    size=emailmsg["volumesize"]
    file = emailmsg["filepath"]
    volume_size = 1024 * 1024 * int(size)
    path = zip_by_volume(file, volume_size)
    pic_list = os.listdir(path)
    print("总共分割"+str(len(pic_list))+"个文件待发送邮件。。。")
    index=0
    for pic in pic_list:
        index+=1
        print("第" + str(index) + "个邮件发送中。。。")
        send_mail(path+"/"+pic,pic,str(index),mail_host,mail_user,mail_pass,sender,receive,msg,header,subject)
    time.sleep(2)
    print("所有邮件发送成功。。。")