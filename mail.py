import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.recipient import recipient

for i in recipient:
    msg = MIMEMultipart()
    msg['From'] = config.login.fromname
    msg['To'] = i
    msg['Subject'] = config.mailcontent.subject

    # Text
    msgText = MIMEText(config.mailcontent.mailtext, 'html')
    msg.attach(msgText)

    # Images
    # wow, nothing here yet!

    server = smtplib.SMTP(config.login.smtp, config.login.port)
    server.starttls()
    server.login(config.login.frommail, config.login.psw)
    text = msg.as_string()
    server.sendmail(config.login.frommail, i, text)
    server.quit()

print('E-mail(s) successfully sent.')