import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart # 메일로 html 전송 할때 필요함
from email import encoders
from email.mime.base import MIMEBase


# ***** SMTP 라이브러리 이용하는 기본 틀 *****
msg = MIMEMultipart('alternative')
content = """
여기에 HTML로 작성가능
<h4>Title<h4>
<button>what<button>
"""
part1 = MIMEText(content, "html")
msg.attach(part1)

# *** 메일에 첨부파일 넣을때 ***
#원하는 파일 rb로 오픈
with open('보낼파일경로', 'rb') as 파일:
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(파일.read())

#파일 base64 인코딩
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="경로제외보낼파일명"')
msg.attach(part)
# *** 첨부파일 파트 ***

msg['Subject'] = 'This is email\'s title'
msg['From'] = 'This is sender - my email address'
msg['To'] = 'Receiver\'s name or email address'
print(msg)

# SMTP(smtp server address, port address)
s = smtplib.SMTP('smtp.naver.com', 587) # NAVER's SMTP server address and port number
s.starttls()
s.login('id', 'pw')
s.sendmail('markkim1@naver.com', 'markkim1@naver.com', msg.as_string())

s.close()
# ********************************************

