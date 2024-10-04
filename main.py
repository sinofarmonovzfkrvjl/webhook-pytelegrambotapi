import telebot
from flask import Flask, request

API_TOKEN = '7596605488:AAHImzVpR__WfikvzT-gFRgZL0vfTd5T1cs'
WEBHOOK_URL = 'https://2990-82-215-107-238.ngrok-free.app/webhook'  # Replace with your URL

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Define a basic handler for messages
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot.")

# Flask route to receive updates from Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

# Set webhook to point to your server URL
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

# Start Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443)
