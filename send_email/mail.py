from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

def sendmail():
    try :
        #pname=input("Enter the name of the person : ")
        #print("Running by default email ids......")
        recipients = ['sauravsen111@gmail.com'] 
        emaillist = [elem.strip().split(',') for elem in recipients]
        msg = MIMEMultipart()
        msg['Subject'] = str("medical suggestion")
        msg['From'] = 'your email'
        msg['Reply-to'] = 'sauravsen111@gmail.com'
         
        msg.preamble = 'Multipart message.\n'
         
        part = MIMEText("the message u want to send")
        msg.attach(part)
         
        part = MIMEApplication(open(str('pic'+".jpg"),"rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=str('pic'+".jpg"))
        msg.attach(part)

        #part = MIMEApplication(open(str(pname+"_suggestion.txt"),"rb").read())
        #part.add_header('Content-Disposition', 'attachment', filename=str(pname+"_suggestion.txt"))
        #msg.attach(part)
         

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login("your email", "your password")
         
        server.sendmail("shauryakhurana809@gmail.com", emaillist , msg.as_string())
    except:
            print("*****Network problem******\n")
    else :  
            print("Sent successfully")
