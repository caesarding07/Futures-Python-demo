'''
Author: CaesarDing
Date: 2021-04-12 15:20:01
LastEditors: CaesarDing
LastEditTime: 2021-04-12 15:52:52
FilePath: \Futures-Python-demo\send_mail.py
Description: 发送邮件
'''
# https://www.runoob.com/python3/python3-smtp.html
# https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=369

#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com" #serve
mail_user="770866225@qq.com" #username
mail_pass="ofaganybecbsbfdf" #token

sender = '770866225@qq.com' #必须和mail_user相同
receivers = ['318407487@qq.com'] #接受邮箱
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
msg = MIMEText('邮件测试msg','plain','utf-8')
msg['From'] = Header('py_bot','utf-8')
msg['To'] = Header('测试','utf-8')

subject = 'Python mail test'
msg['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    #smtpObj.connect(mail_host,25)  # 25为SMTP的端口号
    smtpObj.connect(mail_host,587)  # 括号中对应的是发件人邮箱中的SMTP服务器，端口
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,msg.as_string())
    print("邮件发送成功，请查收")
except smtplib.SMTPException as e:
    print("ERROR: 邮件发送失败，请检查\n",e)
