import smtplib, ssl
from config import EMAIL_PWD, EMAIL_ADDRESS


def send(receiver_email, email_content):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = EMAIL_ADDRESS
    password = EMAIL_PWD
    subject = "A Student is looking for you..."
    message = """Subject: {}\n\n{}""".format(subject, email_content)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
         server.ehlo()
         server.starttls(context=context)
         server.ehlo()
         server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, message)
