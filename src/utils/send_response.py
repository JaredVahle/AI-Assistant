import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import sqlite3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PIL import Image, ImageTk
import tkinter as tk

# Email Notification Function
def send_email(to_email, subject, message):
    from_email = "your_assistant_email@gmail.com"
    password = "your_email_password"
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# Pushbullet Notification Function
def send_pushbullet_notification(api_key, title, body):
    data = {"type": "note", "title": title, "body": body}
    try:
        resp = requests.post("https://api.pushbullet.com/v2/pushes", json=data,
                             headers={"Authorization": f"Bearer {api_key}"})
        if resp.status_code == 200:
            print("Push notification sent!")
        else:
            print("Failed to send push notification:", resp.status_code)
    except Exception as e:
        print("Error sending push notification:", e)

# Google Drive Upload Function
def upload_to_drive(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Authorize with your Google account
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"title": file_path.split('/')[-1]})
    file.SetContentFile(file_path)
    try:
        file.Upload()
        print("File uploaded to Google Drive:", file["alternateLink"])
        return file["alternateLink"]
    except Exception as e:
        print("Failed to upload to Google Drive:", e)
        return None

# Local File Export Function
def save_text_file(content, filename="export.txt"):
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"File saved locally as {filename}")
    except Exception as e:
        print("Failed to save file locally:", e)

# Discord Webhook Notification Function
def send_discord_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("Discord message sent!")
        else:
            print("Failed to send Discord message:", response.status_code)
    except Exception as e:
        print("Error sending Discord message:", e)

# Example Usage of Each Notification/Export Method
if __name__ == "__main__":
    # Email Example
    send_email("recipient@example.com", "Test Subject", "This is a test email message.")

    # Pushbullet Example
    pushbullet_api_key = "your_pushbullet_api_key"
    send_pushbullet_notification(pushbullet_api_key, "Test Push", "This is a test push notification.")

    # Google Drive Example
    file_link = upload_to_drive("sample_file.txt")
    if file_link:
        print("Access the file here:", file_link)

    # Local File Export Example
    save_text_file("This is the content of the exported file.", "exported_text.txt")

    # Discord Webhook Example
    discord_webhook_url = "your_discord_webhook_url"
    send_discord_message(discord_webhook_url, "This is a test message to Discord.")
