# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:22:53 2018

@author: DataTeam
"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time

def write_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('amay396@gmail.com', '1L@stchance')
    while True:
        msg = MIMEMultipart()
        msg['From'] = 'Mom'
        msg['To'] = 'abhay.adav100@gmail.com'
        msg['Subject'] = 'Hello you dirty fucking cunt' 
        body = 'Dear Cuntbag, I just wasted both your time and my time, Merry Chryslera'
        msg.attach(MIMEText(body,'plain'))
        text=msg.as_string()
        server.sendmail('amay396@gmail.com', 'abhay.adav100@gmail.com', text)
        print("Email successfully sent.")
        time.sleep(15)
    server.quit()
def main():
    write_email()
    
if __name__ == "__main__":
    main()
    