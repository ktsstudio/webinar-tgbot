import asyncio
import os

from clients.tg import TgClient


async def run_echo():
    c = TgClient(os.getenv("BOT_TOKEN"))
    offset = 0
    while True:
        res = await c.get_updates_in_objects(offset=offset, timeout=60)
        for item in res.result:
            offset = item.update_id + 1
            await c.send_message(item.message.chat.id, item.message.text)


if __name__ == "__main__":
    asyncio.run(run_echo())
