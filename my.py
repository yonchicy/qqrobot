# -*- coding: utf-8 -*-
import asyncio
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message
from url import get_pictures,photo_dir,delete_pictures
test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)
        if "anime" in message.content:
            _log.info("get pic request ")
            get_pictures()
            photo_name = ""
            for s in os.listdir(photo_dir):
                photo_name = s
                break
            try:
                await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}", file_image=photo_dir+photo_name)
            except Exception as e:
                _log.info("get a timeout reply")
            _log.info("deleting all pictures")
            delete_pictures()
            
        _log.info(message.author.username)
        # await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_guild_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])