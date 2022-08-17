# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
# kenkan
# Aryazakaria
# All rights reserved.



from pyrogram import __version__ as pyver
from pyrogram import idle
import heroku3
from pyrogram.errors import BadRequest
from config import PREFIX, LOG_CHAT, HEROKU_API, HEROKU_APP_NAME
from Poci import app
from Poci.modules import *

app.start()
me = app.get_me()

print(
    f"Poci UserBot started for user {me.first_name}. Type {PREFIX}help in any telegram chat."
)
try:
    if not str(LOG_CHAT).startswith("-100"):
        tai = app.create_supergroup("Logs", "Powered by : @PocongProject\nSupport : @Poconguserbot")
        app.set_chat_photo(tai.id, photo="Poci/sampah/prime.png")
        Heroku = heroku3.from_key(HEROKU_API)
        her = Heroku.app(HEROKU_APP_NAME)
        heroku_var = her.config()
        heroku_var["LOG_CHAT"] = tai.id
    else:
        print("LOG_CHAT, Sudah benar")
    app.send_message(
        LOG_CHAT,
        f"🔥 **PociUserbot Berhasil Di Aktifkan** 🔥\n┌ •**Owner** : [{me.first_name}](tg://user?id={me.id})\n├ •**Pyrogram Version :** `{pyver}`\n├ •**BotVersion  :** `0.0.1`\n├ •**Support By :** @Poconguserbot\n└ •**Channel :** @pocongproject\n\n**Gunakan** `{PREFIX}ping` **untuk cek bot aktif**"
    )
    app.join_chat("PrimeSupportGroup")
    app.join_chat("Poconguserbot")
    app.join_chat("Pocongonlen")
    app.join_chat("gabutan_escape")
    
    idle()
except BadRequest:
    pass
