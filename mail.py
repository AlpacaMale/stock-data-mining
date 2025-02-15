import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


def send_mail(subject, message):
    msg = MIMEMultipart()
    msg["From"] = os.getenv("SENDER_EMAIL")
    msg["To"] = os.getenv("RECEIVER_EMAIL")
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        server.starttls()  # 보안 연결 시작
        server.login(os.getenv("SENDER_EMAIL"), os.getenv("PASSWORD"))  # 로그인
        server.sendmail(
            os.getenv("SENDER_EMAIL"), os.getenv("RECEIVER_EMAIL"), msg.as_string()
        )  # 이메일 전송
        server.quit()
        print("Email transfer success!")
    except Exception as e:
        print("Email transfer failed:", e)
