# _*_ coding: utf-8 _*_
from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from mysql_platform.settings import EMAIL_FROM


def send_user_email(email, send_type="register"):
    # email_record = EmailVerifyRecord()
    code = generate_random_string(random_length=16)
    # email_record.code = code
    # email_record.email = email
    # email_record.send_type = send_type
    # email_record.save()
    # send email to register
    if send_type == 'register':
        email_title = '优朋数据库平台注册'
        email_body = '{0}{1}{2}'.format('http://localhost:8000/active/', code, '/')
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    # send email to reset password
    elif send_type == 'forget':
        email_title = '幕学在线网密码重置链接'
        email_body = '请点击下面的链接重置你的密码：{0}{1}{2}'.format('http://localhost:8000/reset/', code, '/')
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_string(random_length=8):
    string = ''
    chars = 'abdcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        string += chars[random.randint(0, length)]
    return string
