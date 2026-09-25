# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
from pyrogram import utils as pyro_utils
import sys

# ════════════════════════════════════════════════════════════════════════════════
# 🚀 FAST MODE SETTINGS (DOWNLOAD + UPLOAD DONO MAXIMUM)
# ════════════════════════════════════════════════════════════════════════════════

# ✅ FIX 1: Chunk size 8MB (max allowed, download speed boost)
pyro_utils.MIN_CHUNK_SIZE = 8 * 1024 * 1024  # 8MB per chunk

# ✅ FIX 2: Workers 64 (maximum parallel download)
pyro_utils.MAX_WORKERS = 64

# ✅ FIX 3: Concurrent transmissions 32 (zyada chunks ek saath)
if hasattr(pyro_utils, "MAX_CONCURRENT_TRANSMISSIONS"):
    pyro_utils.MAX_CONCURRENT_TRANSMISSIONS = 32

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
    workers=64,          # ✅ 32 se 64 kiya
    sleep_threshold=30,
)

userbot = Client(
    "4gbbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING,
    workers=64,          # ✅ 32 se 64 kiya
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
