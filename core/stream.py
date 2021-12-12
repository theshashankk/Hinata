import re
import asyncio

from Konfig import BOT_USERNAME, IMG_1, IMG_2
from temp.filters import command, other_filters
from temp.queues import QUEUE, add_to_queue
from temp.client_base import call_py, user
from temp.client_base import bot as b
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0
      
async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@b.on_message(filters.command("play") & ~filters.edited)
async def kkplay(client, m: Message):
  replied = m.reply_to_message
  chat_id = m.chat.id
  keyboard = InlineKeyboardMarkup(
    [
      [
        InlinekeyboardButton('⛓️ Open Menu', callback_data='cbmenu')
      ],[
        InlineKeyboardButton('🚧 Close menu', callback_data='cls')
      ]
    ]
  )
  if m.sender_chat:
    await m.reply_text("You're an __Anonymous admin__!!\n\n**Revert back to use me**")
  else:
    await m.reply_text('__Work in process__')
    

print('[PLUGIN] - IMPORTED PLAY')
