#



# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >



from config import MONGO_URI

import motor.motor_asyncio

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
