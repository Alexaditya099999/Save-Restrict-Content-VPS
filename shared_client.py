# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from config import (
    PYRO_CHUNK_SIZE, PYRO_WORKERS, PYRO_MAX_CONCURRENT,
    TELETHON_RETRIES, USE_CRYPTG, USE_IPV6
)
from pyrogram import Client
from pyrogram import utils as pyro_utils
import sys

# ════════════════════════════════════════════════════════════════════════════════
# ░ 🚀 FAST MODE OVERRIDES (Speed Boost)
# ════════════════════════════════════════════════════════════════════════════════

# --- Pyrogram Speed Boost ---
pyro_utils.MIN_CHUNK_SIZE = PYRO_CHUNK_SIZE
pyro_utils.MAX_WORKERS = PYRO_WORKERS
if hasattr(pyro_utils, "MAX_CONCURRENT_TRANSMISSIONS"):
    pyro_utils.MAX_CONCURRENT_TRANSMISSIONS = PYRO_MAX_CONCURRENT

# --- cryptg check ---
if USE_CRYPTG:
    try:
        import cryptg
        print("✅ cryptg loaded — encryption fast mode ON")
    except ImportError:
        print("⚠️ cryptg not installed — run: pip install cryptg")

# ════════════════════════════════════════════════════════════════════════════════
# ░ CLIENT SETUP
# ════════════════════════════════════════════════════════════════════════════════

# Telethon client - fast connection mode
# NOTE: connection_mode argument hata diya kyunki Telethon mein ye support nahi hai
client = TelegramClient(
    "telethonbot",
    API_ID,
    API_HASH,
    connection_retries=TELETHON_RETRIES,
    retry_delay=1,
    auto_reconnect=True,
    use_ipv6=USE_IPV6,
)

# Pyrogram bot client - fast settings
app = Client(
    "pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=PYRO_WORKERS,
    sleep_threshold=30,
    max_concurrent_transmissions=PYRO_MAX_CONCURRENT,
)

# Userbot (premium session) - fast settings
userbot = Client(
    "4gbbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING,
    workers=PYRO_WORKERS,
    sleep_threshold=30,
    max_concurrent_transmissions=PYRO_MAX_CONCURRENT,
) if STRING else None


async def start_client():
    if not client.is_connected():
        await client.start(bot_token=BOT_TOKEN)
        print("SpyLib started (Fast Mode)...")
    if STRING and userbot:
        try:
            await userbot.start()
            print("Userbot started (Fast Mode)...")
        except Exception as e:
            print(f"Hey honey!! check your premium string session, it may be invalid or expired: {e}")
            sys.exit(1)
    await app.start()
    print("Pyro App Started (Fast Mode)...")
    return client, app, userbot
