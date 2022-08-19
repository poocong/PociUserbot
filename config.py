import os
from base64 import b64decode
from dotenv import load_dotenv
load_dotenv()

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
CHANNEL = os.getenv("CHANNEL", "pocongonlen")
GROUP = os.getenv("GROUP", "PocongUserbot")
MONGO_URI = os.getenv("MONGO_URI")
SESSION = os.getenv("SESSION")
PREFIX = os.getenv("PREFIX", ".")
ALIVE_LOGO = os.getenv("ALIVE_LOGO", "https://telegra.ph/file/9375630e45f16fea531bf.jpg")
LOG_CHAT = int(os.getenv("LOG_CHAT", "0"))
HEROKU_API = os.getenv("HEROKU_API", None)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
GIT_TOKEN = os.getenv("GIT_TOKEN", "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")
PM_LOGO = os.getenv("PM_LOGO", "https://telegra.ph/file/9375630e45f16fea531bf.jpg")
BLACKLIST_GCAST = {int(x) for x in os.getenv
                  ("BLACKLIST_GCAST", "").split()}
