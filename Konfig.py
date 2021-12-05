import os
from dotenv import load_dotenv as envv

if os.path.exists('local.env'):
  envv('local.env')
  
envv()
admins = {}

STRING_SESSION = os.environ.get('STRING_SESSION', '')
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
BOT_USERNAME = os.environ.get('BOT_USERNAME', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
PREFIX = os.environ.get('PREFIX', '/ !').split()
DURATION_LIMIT = int(os.environ.get('DURATION_LIMIT', '89027'))
SUDO_USERS = ['2003485925', '1754865180']
IMG_1 = "https://telegra.ph/file/d6f92c979ad96b2031cba.png"
IMG_2 = "https://telegra.ph/file/6213d2673486beca02967.png"
IMG_3 = "https://telegra.ph/file/f02efde766160d3ff52d6.png"
IMG_4 = "https://telegra.ph/file/be5f551acb116292d15ec.png"
