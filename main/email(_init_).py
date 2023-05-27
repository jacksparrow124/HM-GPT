import whisperload
import main 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Email:
    def __init__(self) -> None:
        mailserver = smtplib.SMTP('smtp.gmail.com',)
      

    def SendMail(self):
        msg = MIMEMultipart()
        msg['From'] = ['gpt232323@gmail.com']
        msg['To'] = ['your email adress']
        msg['Subject'] = ['Your Monthly Token Usage And questions asked 🙂']
        message = ('Your monthly spending of tokens is: %i'% tokens)
        msg.attach(MIMEText(message))





