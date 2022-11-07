import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'your_email_here'
email['to'] = 'target_email_here'
email['subject'] = 'salut !'

email.set_content(html.substitute({'name':'Boke'}),'html')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email_here','password_here')
    smtp.send_message(email)
    print('succes')    