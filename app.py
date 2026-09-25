# ✅ Bot ko Flask ke saath chalao
if __name__ == "__main__":
    import subprocess
    import threading

    def run_bot():
        subprocess.run(["python3", "main.py"])

    # Bot ko background thread mein chalao
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

    # Flask server chalao
    app.run(host="0.0.0.0", port=5000)
