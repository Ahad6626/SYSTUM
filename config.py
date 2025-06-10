import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("20798533",))
API_HASH = getenv("12731853464e7518dc3d76570a9bac95",)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7110984051:AAG_IvFlPeI1ocogc30fw46OPRr_5hsAN78",)

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "Systumm_music_bot")

# Get Your repo
REPO_LINK = getenv("REPO_LINK" , "https://t.me/BRANDED_PAID_CC")

# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "Sytumm")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/",)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002729831681",))

# Get this value from @CrewMusic_bot on Telegram by /id
OWNER_ID = int(getenv("7741478148", 6258877205))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/SYSTUM",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("https://t.me/IvanxBeatxBoom", "https://t.me/BRANDRD_BOT")
SUPPORT_CHAT = getenv("https://t.me/ivanxmusic", "https://t.me/BRANDED_WORLD")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("BQFMsJ0ACRpxq_7urLNfQP_9biw1yyBb1A9T3PQKxFFLEXrQD-STKQnqUUY89Yemy947Pb36BIDu-KHSv5XAwTIzfV9-Qp-0w6boi9WH1aTs3y4o63tXkgLJX_CtT6wjlDTtshh2OCfJufCwSOZ7nonJBb1Q45tYAMy3KEmApBDet8A3NuXRc0G-CBC4zf03f-h2kworQn6582f3Z7l2Z9fFhjY4jL8eghumS89XLsJmN9P9-IMWgAACsmlVd67aLIQhrBKisr0mS5N8BMDPEARVLdipNsbLWz6IHv5onR4JTzh_ffxWdLcHDQx1AE8s_29Hhgr859JqZinVcWXN_JX3K8wgtgAAAAG-vn48AA", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/tsfco0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/tsfco0.jpg"
)
PLAYLIST_IMG_URL = "https://i.ibb.co/zTWJGsFc/c0dabf4380ee.jpg"
STATS_IMG_URL = "https://i.ibb.co/zTWJGsFc/c0dabf4380ee.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ce5ffb3d5f383c781f234.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
