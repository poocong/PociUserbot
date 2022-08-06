import os
from base64 import b64decode
from dotenv import load_dotenv
load_dotenv()

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
MONGO_URI = os.getenv("MONGO_URI")
SESSION = os.getenv("SESSION")
PREFIX = os.getenv("PREFIX", ".")
LOGO_POCI = os.getenv("LOGO_POCI", "https://telegra.ph/file/b79ee68a92ec4aa832e19.jpg")
LOG_CHAT = int(os.getenv("LOG_CHAT", "0"))
HEROKU_API = os.getenv("HEROKU_API", None)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
GIT_TOKEN = os.getenv("GIT_TOKEN", "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")
PM_LOGO = os.getenv("PM_LOGO", "https://telegra.ph/file/797ca7b6ec45871ad059d.jpg")
BLACKLIST_GCAST = {int(x) for x in os.getenv
                  ("BLACKLIST_GCAST", "").split()}
