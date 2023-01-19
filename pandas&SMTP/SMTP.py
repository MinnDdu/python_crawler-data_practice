import smtplib
from email.mime.text import MIMEText


# *** SMTP 라이브러리 이용하는 기본 틀 ***
text = 'Hello what is your name?'
msg = MIMEText(text)

msg['Subject'] = 'This is email\'s title'
msg['From'] = 'This is sender'
msg['To'] = 'Receiver\'s name or email address'
print(msg)

s = smtplib.SMTP('naver smtp address')
s.starttls()
s.login('id', 'pw')
s.sendmail('sender', 'receiver', msg.as_string())

s.close()
# ******

