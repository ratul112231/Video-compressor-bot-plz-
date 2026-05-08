from bot.get_cfg import get_config


class Localisation:
    START_TEXT = """Ciao😁,
    
This is <b>🌈Saviour Coders' Video Compressor Bot🌈.</b>

<i>🥇Send any link and it will be Compressed to the desired size.🥇</i>

<b>Click👉</b> /help for more details.

<b>Features of the bot:</b>
<i>🎯Superfast
🎯Responsive 
🎯Easy to use</i>

<b>Support Group</b> :- ⛵️@ubuntu_coders⛵️
<b>Support Channel</b> :- 💈@UCbotchannel💈
<b>My Master</b> :- 🔮@saviour_coder🔮"""
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading 📥 \n"
    
    UPLOAD_START = "📤 Uploading 📤 \n"
    
    COMPRESS_START = "📀 Trying to compress... 📀"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to delete existing media. ⚠️"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi I am <b>🦋Saviour Coder Video Compressor Bot🦋</b> \n\n1. <i>Sent your telegram big video file</i> \n2. <i>Reply the file - /compress And enter the Persentage to which you want to compress</i> \n\n👉🏻Eg:- <code>/compress 50</code> compresses the video to 50%👈🏻 \n\nSupport Group :@ubuntu_coders"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
