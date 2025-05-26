import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

def send_verification_email(email_to: str, token: str):
    message = MIMEMultipart()
    message["From"] = settings.EMAIL_USERNAME
    message["To"] = email_to
    message["Subject"] = "Account Verification"
    
    body = f"""
    <h1>Verify Your Account</h1>
    <p>Click the link below to verify your account:</p>
    <a href="http://localhost:8000/auth/verify-email?token={token}">Verify Now</a>
    """
    
    message.attach(MIMEText(body, "html"))
    
    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
        server.send_message(message)