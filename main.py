import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
load_dotenv()
app = Flask('')

@app.route('/')
def home():
    return "rnuing"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="뭐", intents=intents, self_bot=True, help_command=None)

@bot.event
async def on_ready():
    print(f"login")

@bot.command()
async def 하세요(ctx):
    await ctx.send("장난 치시는건가")

if __name__ == "__main__":
    keep_alive()    
    token = os.getenv("token")
    if token:
        bot.run(token)
    else:
        print("er")
