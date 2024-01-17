from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27957041"))
    API_HASH = getenv("API_HASH", "2ae1c9912cd2efdecae7f0208994f0b0")
    BOT_TOKEN = getenv("BOT_TOKEN", "6938329222:AAEpI_f_LqjWfzDUPd9_18T3xkmAl1OEkE4")
    FSUB = getenv("FSUB", "Autosaccept_bot")
    CHID = int(getenv("CHID", "-1625255240"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Allsvdgang:<Single_1122334455>@cluster0001.xrucpqp.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
