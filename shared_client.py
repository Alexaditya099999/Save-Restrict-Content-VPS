# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
from pyrogram import utils as pyro_utils
import sys

# ════════════════════════════════════════════════════════════════════════════════
# 🚀 FAST MODE SETTINGS (DOWNLOAD + UPLOAD DONO FAST)
# ════════════════════════════════════════════════════════════════════════════════

# ✅ FIX: Chunk size ko 1MB se badha kar 4MB kiya (download speed boost)
pyro_utils.MIN_CHUNK_SIZE = 4 * 1024 * 1024  # 4MB per chunk

# ✅ FIX: Workers badha diye (parallel download)
pyro_utils.MAX_WORKERS = 32  # Pehle 24 tha, ab 32

# ✅ FIX: Concurrent transmissions badha diye (ek saath zyada chunks download honge)
if hasattr(pyro_utils, "MAX_CONCURRENT_TRANSMISSIONS"):
    pyro_utils.MAX_CONCURRENT_TRANSMISSIONS = 24  # Pehle 12 tha, ab 24

try:
    import cryptg
    print("✅ cryptg loaded — encryption fast mode ON")
except ImportError:
    print("⚠️ cryptg not installed — run: pip install cryptg")

# ════════════════════════════════════════════════════════════════════════════════
# ░ CLIENT SETUP (DOWNLOAD + UPLOAD DONO FAST)
# ════════════════════════════════════════════════════════════════════════════════

client = TelegramClient("telethonbot", API_ID, API_HASH)

app = Client(
    "pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=32,          # ✅ 24 se 32 kiya (download + upload parallel)
    sleep_threshold=30,
)

userbot = Client(
    "4gbbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING,
    workers=32,          # ✅ 24 se 32 kiya
    sleep_threshold=30,
) if STRING else None

async def start_client():
    if not client.is_connected():
        await client.start(bot_token=BOT_TOKEN)
        print("SpyLib started...")
    if STRING and userbot:
        try:
            await userbot.start()
            print("Userbot started...")
        except Exception as e:
            print(f"Hey honey!! check your premium string session, it may be invalid or expired: {e}")
            sys.exit(1)
    await app.start()
    print("Pyro App Started...")
    return client, app, userbot
