#
#
#
#




from config import MONGO_URI

import motor.motor_asyncio

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
