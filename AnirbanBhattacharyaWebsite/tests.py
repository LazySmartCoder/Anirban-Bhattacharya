import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
msg = MIMEMultipart()
msg['From'] = formataddr((str(Header('Anirban Bhattacharya')), 'contact@anirbanbhattacharya.in'))
msg['To'] = 'anirbanbhattacharya.me@gmail.com'
msg["Subject"] = "HI"
html = "<h1>Thanks</h1>"
msg.attach(MIMEText(html, 'html'))
s = smtplib.SMTP('send.smtp.mailtrap.io', port=587)
s.starttls()
s.login("api", "855beba793a0cab223a21c3e912dd30d")
s.sendmail('contact@anirbanbhattacharya.in', 'anirbanbhattacharya.me@gmail.com', msg.as_string())
s.quit()