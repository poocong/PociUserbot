# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from config import BOT_VER, CHANNEL, GROUP
from config import CMD_HANDLER as cmd
from PociUb import CMD_HELP, StartTime
from PociUb.helpers.basic import edit_or_reply
from PociUb.helpers.PyroHelpers import ReplyCheck
from PociUb.helpers.SQL.globals import gvarstatus
from PociUb.helpers.tools import convert_to_image
from PociUb.utils import get_readable_time
from PociUb.utils.misc import restart

from .help import add_command_help

modules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or "https://telegra.ph/file/78dfef3f9342fe7058281.jpg"
)


@Client.on_message(filters.command(["alive", "awake"], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "⚡️")
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"**[PociUb](https://github.com/poocong/PociUserbot) is Up and Running.**\n\n"
        f" <b>Master :</b> {client.me.mention} \n"
        f" <b>Modules :</b> <code>{len(modules)} Modules</code> \n"
        f" <b>Bot Version :</b> <code>{BOT_VER}</code> \n"
        f" <b>Python Version :</b> <code>{python_version()}</code> \n"
        f" <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f" <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"    **[𝚂𝚞𝚙𝚙𝚘𝚛𝚝](https://t.me/{GROUP})** | **[𝙲𝚑𝚊𝚗𝚗𝚎𝚕](https://t.me/{CHANNEL})** | **[𝙾𝚠𝚗𝚎𝚛](tg://user?id={client.me.id})**"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(man, disable_web_page_preview=True)


@Client.on_message(filters.command("setalivelogo", cmd) & filters.me)
async def setalivelogo(client: Client, message: Message):
    try:
        import PociUb.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    Man = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Man.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await Man.edit(
        f"**Berhasil Mengcustom ALIVE LOGO Menjadi {link}**",
        disable_web_page_preview=True,
    )
    restart()


add_command_help(
    "alive",
    [
        [
            "alive",
            "Untuk memeriksa userbot anda berfungsi atau tidak",
        ],
        [
            "setalivelogo  <reply ke foto/video/gif>",
            "Untuk mengcustom alive logo userbot anda",
        ],
    ],
)
