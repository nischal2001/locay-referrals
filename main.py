from flask import Flask
import threading
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def start_bot():
    subprocess.run(["python", "telegram_interface/telegram_bot.py"])

thread = threading.Thread(target=start_bot)
thread.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)