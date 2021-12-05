import asyncio
from pytgcalls import idle
from temp.client_base import call_py, bot

async def mulai_bot():
    print("[HINATA]: STARTING BOT CLIENT")
    await bot.start()
    print("[HINATA]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[HINATA]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
