# original module https://raw.githubusercontent.com/KeyZenD/modules/master/MirrorFlipV2.py | t.me/the_kzd
import os

from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HANDLER as cmd
from .help import add_command_help

from PIL import Image, ImageOps


async def make(client, message, o):
    reply = message.reply_to_message
    if reply.photo or reply.sticker:
        if reply.photo:
            downloads = await client.download_media(reply.photo.file_id)
        else:
            downloads = await client.download_media(reply.sticker.file_id)
        path = f"{downloads}"
        img = Image.open(path)
        await message.delete()
        w, h = img.size
        if o in [1, 2]:
            if o == 2:
                img = ImageOps.mirror(img)
            part = img.crop([0, 0, w // 2, h])
            img = ImageOps.mirror(img)
        else:
            if o == 4:
                img = ImageOps.flip(img)
            part = img.crop([0, 0, w, h // 2])
            img = ImageOps.flip(img)
        img.paste(part, (0, 0))
        img.save(path)
        if reply.photo:
            return await reply.reply_photo(photo=path)
        elif reply.sticker:
            return await reply.reply_sticker(sticker=path)
        os.remove(path)

    return await message.edit("<b>Need to answer the photo/sticker</b>")


@Client.on_message(filters.command(["ll", "rr", "dd", "uu"], cmd) & filters.me)
async def mirror_flip(client: Client, message: Message):
    await message.edit("<b>Processing...</b>")
    param = {"ll": 1, "rr": 2, "dd": 3, "uu": 4}[message.command[0]]
    await make(client, message, param)

add_command_help(
    "stikerv2",
    [
        ["rr", "[reply stiker] reflects the left side"],
        ["ll", "[reply stiker] reflects the left side"],
        ["dd", "[reply stiker] reflects the bottom"],
        ["uu", "[reply stiker] reflects the top"],
    ],
)
