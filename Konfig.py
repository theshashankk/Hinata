import os
from dotenv import load_dotenv as envv

if os.path.exists('local.env'):
  envv('local.env')
  
load_dotenv()
admins = {}

STRING_SESSION = os.environ.get('STRING_SESSION', '')
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
BOT_TOKEN = os.environ.get('TOKEN', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
PREFIX = os.environ.get('PREFIX', '/ !').split())
DURATION_LIMIT = int(os.environ.get('DURATION_LIMIT', '89027'))
SUDO_USER = int (os.environ.get('SUDO_USER', '').split())
