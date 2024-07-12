import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "gy2452jvyvgb33la@ethereal.email"
    login = "gy2452jvyvgb33la@ethereal.email"
    password = "w9VJPDsKFkdNVUnDEy"

    mgs = MIMEMultipart()
    mgs["from"] = "Viagens_confirmar@gmail.com"
    mgs["to"] = ", ".join(to_addrs)
    mgs["subject"] = "Confirmação de viagem"
    mgs.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = mgs.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    
    server.quit()