import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()


class EmailService:

    @staticmethod
    def send_email(to_email, subject, body):

        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_email = os.getenv("SMTP_EMAIL")
        smtp_password = os.getenv("SMTP_PASSWORD")

        print("SMTP_SERVER:", smtp_server)
        print("SMTP_EMAIL:", smtp_email)

        msg = MIMEMultipart()
        msg["From"] = smtp_email
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        try:

            print("Connecting to SMTP server...")

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            print("Logging in...")

            server.login(smtp_email, smtp_password)

            print("Sending email...")

            server.send_message(msg)

            server.quit()

            print(f"Email sent to {to_email}")

            return True

        except Exception as e:

            print("Email sending failed:", e)

            return False