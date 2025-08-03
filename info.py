import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '29340297'))
API_HASH = environ.get('API_HASH', '72bede8730c879055b24b8147c5a05fb')
BOT_TOKEN = environ.get('BOT_TOKEN', '7863680704:AAFqZ3PRFfaSvrHw1k4y5vQE8WLbl0W0EGU')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5999685383').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/UchihaClan007")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002229376403'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+yMp396Y1fjQyYTY9')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002437618797').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://aliakhtae5:GoqDgw7jbZ4IOGPh@cluster0.nl5vm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002419512905'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/7101b3c8f07334d93e925-c5c7dcfcd8c0d269ec.jpg')
START_IMG = environ.get('START_IMG', 'https://graph.org/file/96432b7f0a4dda8f35df5-d1892521e9beb56d32.jpg')
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002486915650'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002344221556'))
URL = environ.get('URL', 'mytestbot-jvdfhbj.com')
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002486915650'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/rhhdhdjs")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/498858bd81f7cb76b185d-aac6fcb26a702d8818.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "d782d673a2f68126bfe29cf393546b4a88411771")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'mdiskshortner.link')
SHORTENER_API2 = environ.get("SHORTENER_API2", "41a89e7a1f16e7dbec0ee52d743f3b5a38a09613")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'shortslink2.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "f287e7e9b1a23c34f542f77787d39607cae36a4d")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'shortslink3.online')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-100'))
request_channel = environ.get('REQUEST_CHANNEL', '-100')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002203977455'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}

