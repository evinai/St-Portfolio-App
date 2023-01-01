import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "ttunca@evin-ai.com"
password = "htcolqlotwzowlyj"

receiver = "ttunca@evin-ai.com"
context = ssl.create_default_context()


message = """\
Subject: Hi!,
How are You?
Bye
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)