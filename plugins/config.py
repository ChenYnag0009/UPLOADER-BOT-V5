import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7675355288:AAFfpULkl1w0mVmO2nrLlPNLyiXnDC13N8M")
    
    API_ID = int(os.environ.get("API_ID", "17822365"))
    
    API_HASH = os.environ.get("API_HASH", "b561a326f3d3e7e6ef41cf7d57ab8fb3")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = ""
    
    FREE_USER_MAX_FILE_SIZE = 2097152000

    MAX_SPLIT_SIZE = 4187407334
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    DEF_WATER_MARK_FILE = "@UploaderXNTBot"
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://pangphu9:0pSRO3UHIoH5ouAx@cluster0.ipqp2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002342176606"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002034379731")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "8079310657"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "URL_Uploader_QingYang_Bot")
                                  
