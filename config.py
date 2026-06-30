from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
STRING_SESSION = getenv("STRING_SESSION")
MONGO_URI = getenv("MONGO_URI")

OWNER_ID = int(getenv("OWNER_ID", 0))
LOG_GROUP = int(getenv("LOG_GROUP", 0))

SUPPORT_CHAT = getenv("SUPPORT_CHAT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
