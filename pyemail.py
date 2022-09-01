#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import config
import email


def send_mail(email_server, email_port, receiver_email, title, to_send, sender_email_account=config.sender_email_account, sender_email_password=config.sender_email_password, sender_name=config.sender_name, receiver_name=config.receiver_name):

    msg = email.mime.text.MIMEText(to_send, 'plain', 'utf-8')
    msg['From'] = email.utils.formataddr([sender_name, sender_email_account])
    msg['To'] = email.utils.formataddr([receiver_name, receiver_email])
    msg['Subject'] = title

    server = smtplib.SMTP_SSL(email_server, email_port)
    server.login(sender_email_account, sender_email_password)

    server.sendmail(sender_email_account, [receiver_email], msg.as_string())
    server.quit()
