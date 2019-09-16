import os
import imaplib
import email
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from app import config
from app import identify

def checkformail():
    mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
    mail.login(config.IMAP_EMAIL, config.IMAP_PASSWORD)
    mail.select('inbox')

    type, emails = mail.search(None, '(UNSEEN)')
    mail_ids = emails[0]
    email_id_list = mail_ids.split()

    attach_dir = os.path.join(config.APP_PATH, 'attachments')
    if not os.path.exists(attach_dir):
        os.mkdir(attach_dir)

    for id_email in email_id_list:
        typ, messageParts = mail.fetch(id_email, '(RFC822)' ) # i is the email id
        
        emailBody = messageParts[0][1]
        thismail = email.message_from_string(emailBody.decode('utf-8'))
        sender = thismail['From']
        
        for part in thismail.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue
            fileName = part.get_filename()

            if bool(fileName):
                #filePath = os.path.join(attach_dir, fileName)
                filePath = os.path.join(attach_dir, 'attach')
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

                filePathJpg = filePath + '.jpg'

                # convert to .jpg:
                os.system('convert ' + filePath + ' ' + filePathJpg)

                filePath2 = os.path.join(attach_dir, 'attachout.jpg')
                identify.identify_image(filePath, filePath2)
                print('Sending email response to: ' + sender)
                sendnewemail(sender)
    
    mail.close()
    mail.logout()
    

def sendnewemail(toaddr):   
    fromaddr = config.IMAP_EMAIL
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Result (what's this?)"
    
    # string to store the body of the mail 
    body = "Hello, the bot has analyzed your image.  The result is attached.  Thank you."
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    attach_dir = os.path.join(config.APP_PATH, 'attachments')
    filePath2 = os.path.join(attach_dir, 'attachout.jpg')
    filename = "image.jpg"
    attachment = open(filePath2, "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, config.IMAP_PASSWORD) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 