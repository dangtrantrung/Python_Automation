import os
import smtplib
import ssl
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

print(os.getcwd())
os.chdir(r"E:\Python_Automation\Python for Networking\Simple Mail Client")

filename='password.txt'
read_f=open(filename,mode='r')
password=read_f.readline()
read_f.close()
print(password)

#fromaddr='celinediontrung@yahoo.com.vn'
fromaddr='trung280584@gmail.com'

msg = EmailMessage()
msg.set_content("The body of the email is here")
msg["Subject"] = "An Email Alert"
msg["From"] = fromaddr
msg["To"] = "trung280584@gmail.com"

server, port, connect_method = (
    'smtp.mail.yahoo.com', 465, smtplib.SMTP_SSL) if 'yahoo.com' in fromaddr else (
    'smtp.gmail.com', 587, smtplib.SMTP)
smtpserver=connect_method(server, port)
smtpserver.set_debuglevel(1)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login("trung280584@gmail.com", password)
smtpserver.sendmail(msg)
