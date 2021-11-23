import dotenv
import os

env = os.path.join(os.path.dirname(__file__), 'creds/.env')
dotenv.load_dotenv(env)

try:
    DISCORD_AUTH = str(os.environ['DISCORD_AUTH'])
    NOTION_AUTH = str(os.environ["NOTION_AUTH"])
    DATABASE = str(os.environ["DATABASE_TOKEN"])
except:
    print("Invalid token")

