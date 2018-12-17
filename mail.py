import smtplib
from config.login import *
from config.mailcontent import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.recipient import recipient

for i in range(len(recipient)):
    msg = MIMEMultipart()
    msg['From'] = fromname
    msg['To'] = recipient[i]
    msg['Subject'] = subject

    # Text
    msgText = MIMEText(mailtext, 'html')
    msg.attach(msgText)

    # Images
    # wow, nothing here yet!

    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(frommail, psw)
    text = msg.as_string()
    server.sendmail(frommail, recipient[i], text)
    server.quit()

print('E-mail(s) successfully sent.')