import requests
import smtplib
import os

from email.message import EmailMessage
from bs4 import BeautifulSoup

GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

response = requests.get("https://vg.no")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

email = "Her er alle VG-artiklene på forsiden:\n\n"
email += "<ul>\n"

for article in articles:
  title = article.text.strip().removesuffix("VG+").replace("\n", " ").replace("  ", " ")

  link = article.a['href']

  email += f"<li><a href='https://vg.no{link}'>{title}</a></li>\n\n"
email += "\n</ul>"

msg = EmailMessage()
msg['Subject'] = 'Daglig oppsummering av VG-artikler'
msg['From'] = 'jotjernshaugen@gmail.com'
msg['To'] = 'jotjernshaugen@gmail.com'
msg.set_content(email, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('jotjernshaugen@gmail.com', GMAIL_APP_PASSWORD)
    smtp.send_message(msg)

