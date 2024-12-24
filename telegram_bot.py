import telegram
from telegram.ext import Updater, CommandHandler
import json
from agent import AIAgent

def load_telegram_config():
    try:
        with open('telegram_config.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Error: telegram_config.json not found.")
        return None

telegram_config = load_telegram_config()
if not telegram_config:
    exit()

bot = telegram.Bot(token=telegram_config['telegram_bot_token'])

agent = AIAgent(
    name="Gingerbread AI",
    personality="cheerful, sweet, and spicy 🍪",
    task_list=["greet", "joke", "story", "calculation"],
    settings={"openai_api_key": "YOUR_OPENAI_API_KEY"}
)

def greet(update, context):
    user_name = update.message.from_user.first_name
    update.message.reply_text(f"Hello, {user_name}! Welcome to Gingerbread AI 🍪")

def joke(update, context):
    jokes = [
        "Why did the gingerbread man go to therapy? Because he was feeling crumby!",
        "What’s a gingerbread man’s favorite genre of music
