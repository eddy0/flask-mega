from flask import render_template, current_app
from flask_mail import Message

import config
import secret
from threading import Thread
from marrow.mailer import Mailer, Message


def configured_mail():
    config = {
        # 'manager.use': 'futures',
        'transport.use': 'smtp',
        'transprt.debug': True,
        'transprt.timeout': 1,
        'transport.host': 'smtp.gmail.com',
        'transport.port': 465,
        'transport.tls': 'ssl',
        'transport.username': secret.username,
        'transport.password': secret.password,
        'transport.max_messages_per_connection': 5
    }
    m = Mailer(config)
    m.start()
    return m

mailer = configured_mail()

print('mailer', mailer)


def send_async_email(app, msg):
    with app.app_context():
        mailer.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject=subject, author=sender, to=recipients)
    msg.plain = text_body
    msg.rich = html_body
    print('mg', msg)
    mailer.send(msg)
    # Thread(target=send_async_email, args=(current_app, msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    print('user', user.email)
    send_email('[Microblog] Reset Your Password',
               sender='{}@gmail.com'.format(secret.username),
               recipients=user.email,
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('reset_password.html',
                                         user=user, token=token)
               )
