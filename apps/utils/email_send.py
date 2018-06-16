from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from NeuOnline.settings import EMAIL_FROM


def generate_random_str(randomlenth=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlenth):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    random_string = generate_random_str(16)
    email_record.code = random_string
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "东软睿道在线网激活链接"
        email_body = "请点击以下链接激活你的账号：http://localhost:8000/active/{0}".format(random_string)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email,])
        print(send_status)
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "东软睿道在线网密码找回"
        email_body = "请点击以下找回你的密码：http://localhost:8000/reset/{0}".format(random_string)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email, ])
        print(send_status)
        if send_status:
            pass