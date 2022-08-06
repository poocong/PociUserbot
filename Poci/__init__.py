# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
# kenkan
#
# All rights reserved.

import logging
import time

from pyrogram import Client, errors
from config import API_HASH, API_ID, SESSION
from Poci.database.git import git

git()
HELP = {}
CMD_HELP = {}
StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH
SESSION = SESSION

app = Client(
    session_string=SESSION,
    api_id=API_ID, 
    api_hash=API_HASH,
    name="Poci",
    in_memory=True
)

