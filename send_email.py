import smtplib, ssl
host = "smtp.gmail.com"
port = 465
username = "farukh.mushtaq@gmail.com"
password ="kcfkmnjfqennwjpt"
context = ssl.create_default_context()

reciever = "pakipcs@yahoo.com"
# Following is format of message, Subject should be written
# in same format. """\ is must. to avoid break for subject.
message = """\
Subject: This is Test Email From Python
Aoa,
This is 
test email from Python web project, contact us page
Regards
Farukh Mushtaq
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,reciever,message)
