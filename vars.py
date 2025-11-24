import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "25933223"))
API_HASH = os.environ.get("API_HASH", "6ef5a426d85b7f01562a41e6416791d3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

CREDIT = os.environ.get("CREDIT", "𝕮𝖍𝖔𝖙𝖆 𝕭𝖍𝖊𝖊𝖒")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "UGxPRO")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sujalbot:sujalbot@cluster0.mnjoqfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
ADMINS = [8599768268, 1570359763] 


# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://www.chhotabheem.com/image/catalog/wallpaper/series_03.jpg").split()))

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin @ItsUGBot to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}









