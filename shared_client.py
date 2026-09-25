# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
from pyrogram import utils as pyro_utils
import sys

# ════════════════════════════════════════════════════════════════════════════════
# 🚀 FAST MODE SETTINGS (DOWNLOAD + UPLOAD DONO FAST, DB SAFE)
# ════════════════════════════════════════════════════════════════════════════════

# ✅ Chunk size 4MB (fast download, DB pe load nahi)
pyro_utils.MIN_CHUNK_SIZE = 4 * 1024 * 1024

# ✅ Workers 24 (pehle jitna tha, DB crash nahi hoga)
pyro_utils.MAX_WORKERS = 24

# ✅ Concurrent transmissions 12 (balanced)
if hasattr(pyro_utils, "MAX_CONCURRENT_TRANSMISSIONS"):
    pyro_utils.MAX_CONCURRENT_TRANSMISSIONS = 12

try:
    import cryptg
    print("✅ cryptg loaded — encryption fast mode ON")
except ImportError:
    print("⚠️ cryptg not installed — run: pip install cryptg")

# ════════════════════════════════════════════════════════════════════════════════
# ░ CLIENT SETUP
# ════════════════════════════════════════════════════════════════════════════════

client = TelegramClient("telethonbot", API_ID, API_HASH)

app = Client(
    "pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=24,          # ✅ 64 se 24 kiya (DB safe)
    sleep_threshold=30,
)

userbot = Client(
    "4gbbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING,
    workers=24,          # ✅ 64 se 24 kiya
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
