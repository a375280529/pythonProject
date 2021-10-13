#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "729143240"  # 用户名
mail_pass = "uvedjyaeaghwbfgb"  # 口令

sender = '729143240@qq.com'
receivers = ['375280529@qq.com','309826528@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

ms="""
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""

# 邮件正文是MIMEText
msg = MIMEText(ms, 'html', 'utf-8')
# 邮件对象
message = MIMEMultipart()
message['From'] = Header("测试邮件", 'utf-8')
#message['To'] = Header('zxc', 'utf-8')
message['To']=";".join(receivers)
message['date']=time.strftime("%a,%d %b %Y %H:%M:%S %z")

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
message.attach(msg)

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('aa.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("except: 无法发送邮件")