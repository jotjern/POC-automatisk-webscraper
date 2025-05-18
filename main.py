import urllib.parse
import requests
import smtplib
import os

from email.message import EmailMessage
from bs4 import BeautifulSoup
import urllib

GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

response = requests.get("https://vg.no")
response.raise_for_status()

website = BeautifulSoup(response.text, "html.parser")

email = "Her er alle VG-artiklene på forsiden:\n\n"

for article in website.find_all("article"):
  title = article.text.strip()
  # Fjern linjeskift og ekstra mellomrom
  title = title.replace("\n", " ").replace("  ", " ")

  link = article.find("a")

  url = "https://www.vg.no" + link["href"]

  email += title + ": " + url + "\n"
email += "\n"

msg = EmailMessage()
msg['Subject'] = 'Liste over VG-artikler'
msg['From'] = 'jotjernshaugen@gmail.com'
msg['To'] = 'jotjernshaugen@gmail.com'
msg.set_content(email)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('jotjernshaugen@gmail.com', GMAIL_APP_PASSWORD)
    smtp.send_message(msg)

print("Email sent successfully!")