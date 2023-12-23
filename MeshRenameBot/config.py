from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, ""]
        API_HASH = [str, "1f5343b0646645ca1eaf7c4759fc248f"]
        API_ID = [int, 26376042]
        BOT_TOKEN = [str, "6430230017:AAEzPGiVtyeFTuhwMhkcAz9m2PjJklg6mQY"]
        COMPLETED_STR = [str, "█"]
        REMAINING_STR = [str, "▒"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[2036803347]]
        OWNER_ID = [int, 2036803347]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"ANI_BOTS_UPDATES"]
        FORCEJOIN_ID = [int,-1001918398170]

        TRACE_CHANNEL = [int, -1001918398170]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
