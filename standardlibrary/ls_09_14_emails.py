from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib
# mime = multipurpose internet mail extensions

template = Template(Path("standardlibrary/template.html").read_text())
# template.substitute()

message = MIMEMultipart()
message["from"] = "Jonathan Pavkov"
message["to"] = "jonny.pavkov@gmail.com"
message["subject"] = "Bold Email Three"
body = template.substitute({"name": "Jonny Boy"})
# body = template.substitute(name="Jonny Boy")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("standardlibrary/moon.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # transport layer security
    smtp.login("jonathan.pavkov@gmail.com", "syxv opqx xnsh vbcw")
    smtp.send_message(message)
    print("Sent...")
