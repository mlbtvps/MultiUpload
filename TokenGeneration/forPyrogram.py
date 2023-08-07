import asyncio
from pyrogram import Client


#get your api_id and api_hash from https://my.telegram.org/apps
api_id = 27486644  # your api_id
api_hash = "149f309eb1c416c8edac85bba6c5eec2" # your api_hash


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
