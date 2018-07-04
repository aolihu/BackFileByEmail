#!/usr/bin/env python3 
#coding: utf-8 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 

#SMTP server with username and password
smtpserver = '*' 
username = '*' 
password = '' 

#Email sender, receiver and subject
sender = '*' 
receiver = '*' 
subject = '*' 


# Email subject 
msgRoot = MIMEMultipart('related') 
msgRoot['Subject'] = subject
 
#add attachment
att = MIMEText(open('C:\\*', 'rb').read(), 'base64', 'utf-8') 
att["Content-Type"] = 'application/octet-stream' 
att["Content-Disposition"] = 'attachment; filename="*.*"' 
msgRoot.attach(att) 
     
smtp = smtplib.SMTP() 
smtp.connect(smtpserver) 
smtp.login(username, password) 
smtp.sendmail(sender, receiver, msgRoot.as_string()) 
smtp.quit()