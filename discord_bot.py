import discord
import json
from discord.ext import commands
from agent import AIAgent

# Load the Discord configuration
def load_discord_config():
    try:
        with open('discord_config.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Error: discord_config.json not found.")
        return None

discord_config = load_discord_config()
if not discord_config:
    exit()

# Initialize the bot with the command prefix from the config
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=discord_config['command_prefix'], intents=intents)

# Initialize the agent (ensure you've loaded your settings and agent config correctly)
agent = AIAgent(
    name="Gingerbread AI",
    personality="cheerful, sweet, and spicy 🍪",
    task_list=["greet", "joke", "story", "calculation"],
    settings={"openai_api_key": "YOUR_OPENAI_API_KEY"}
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Connected to server: {discord_config["discord_server_id"]}')

@bot.command(name='greet')
async def greet(ctx):
    await ctx.send(f"Hello, {ctx.author.display_name}! Welcome to Gingerbread AI 🍪")

@bot.command(name='joke')
async def joke(ctx):
    jokes = [
        "Why did the gingerbread man go to therapy? Because he was feeling crumby!",
        "What’s a gingerbread man’s favorite genre of music? Crumbs!",
        "Why did the gingerbread cookie break up with the candy cane? They were just too sweet together!"
    ]
    await ctx.send(f"Here's a gingerbread joke for you: {jokes[0]}")

@bot.command(name='generate_image')
async def generate_image(ctx, *, prompt=None):
    if prompt is None:
        prompt = "A cute gingerbread man with a smiling face, standing in front of a decorated Christmas tree."
    
    image_url = agent.generate_image(prompt)
    await ctx.send(f"Here is the gingerbread image you requested: {image_url}")

@bot.command(name='info')
async def info(ctx):
    await ctx.send(f"Hello! I'm Gingerbread AI 🍪, here to make your day sweeter!")

bot.run(discord_config['discord_bot_token'])
