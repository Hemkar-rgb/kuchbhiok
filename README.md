
## Deploy Via Buttons

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/mrgadhvii-os/UGxUploaderv2.git)


```vars.py change```

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

CREDIT = os.environ.get("CREDIT", "〱ＵＧ▕")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "UGxPRO")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://botexe:botexe@cluster0.pqc0ykw.mongodb.net/")
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "77"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "774").split()]  # Default to owner ID

# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://www.chhotabheem.com/image/catalog/wallpaper/Bheem_the_fighter.jpg").split()))

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))


YH SAB ME APNA DATA DAL DO
