import os
import yt_dlp
from telegram.ext import ApplicationBuilder

TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()
git add .
git commit -m "update token to env"
git push
