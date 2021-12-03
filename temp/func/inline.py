from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def music_or_video_keyboard(user_id: int, streaming_status: str):
  keyboard = []
  number = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
  for count, j in enumerate(number):
    keyboard.append(
      InlineKeyboardButton(f'{j}', callback_data='{streaming_status} {count}|{user_id}'
      )
    )
  return keyboard

def process_button(user_id: int, streaming_status: str):
  board = music_or_video_keyboard(user_id, streaming_status)
  temp = []
  keyboard = []
  for count, button in enumerate(board, start=1):
    temp.append(button)
    if count % 3 == 0:
      keyboard.append(temp)
      temp = []
    if count == len(board):
      keyboard.append(temp)
  return keyboard
