import discord
from dotenv import load_dotenv
import os
from jjklist import Phrases
import random

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Domain Expansion")
async def gojo(ctx):
    response = random.choice(Phrases.phrases)
    await ctx.respond(response)

@bot.slash_command(description="Add a statement to the list")
async def add(ctx, statement):
    Phrases.phrases.append(statement)
    await ctx.respond(f"Successfully added `{statement}` to the list.")

bot.run(os.getenv("TOKEN"))