import asyncio

from bot.poller import Poller
from bot.worker import Worker


class Bot:
    def __init__(self, token: str, n: int):
        self.queue = asyncio.Queue()
        self.poller = Poller(token, self.queue)
        self.worker = Worker(token, self.queue, n)

    async def start(self):
        await self.poller.start()
        await self.worker.start()

    async def stop(self):
        await self.poller.stop()
        await self.worker.stop()
