from pyrogram import Client, filters
from pyrogram.types import Message
from temp.client_base import bot as b
from pyrogram.types import (
  InlineKeyboardMarkup,
  InlineKeyboardButton,
  Message
)

@b.on_message(filters.command("start") & ~filters.edited)
async def ok(client, message):
  buttons = InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton('Comming soon....', callback_data='soon')
      ]
    ]
  )
  await message.reply_text('Comming soon', reply_markup=buttons)
