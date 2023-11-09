from os import path, getenv

class Config:
    BOT_OWNER = getenv("BOT_OWNER", "Crazy_Prince")
    API_ID = int(getenv("API_ID", "21352032"))
    API_HASH = getenv("API_HASH", "ef5212c9c99bf568623e22aa89bd4f80")
    BOT_TOKEN = getenv("BOT_TOKEN", "6898920524:AAF7Cw91bTIUsruQw_t0hoZhp94KfNbj2S4")

config = Config()
