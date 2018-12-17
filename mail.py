import smtplib
from config.login import *
from config.mailcontent import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.recipient import recipient

msg = MIMEMultipart()
msg['From'] = frommail
msg['To'] = ', '.join(recipient)
msg['Subject'] = subject

# Text
msgText = MIMEText(mail, 'html')
msg.attach(msgText)

# Images
# wow, nothing here yet!

server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(frommail, psw)
text = msg.as_string()
server.sendmail(frommail, recipient, text)
server.quit()

print("E-mail successfully sent.")