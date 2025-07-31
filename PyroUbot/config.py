
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "6414604963").split()))

API_ID = int(os.getenv("API_ID", "28897396"))

API_HASH = os.getenv("API_HASH", "b2db2096462fc504a8585707b9775e41")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8241128314:AAGX2eaLVHh4zvUCNqdIeXl1X0zFXZ3AeFo")

OWNER_ID = int(os.getenv("OWNER_ID", "6414604963"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002419662880").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002511504837"))
