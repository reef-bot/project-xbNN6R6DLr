# bot.py

import discord
from discord.ext import commands
import json

# Import all other necessary files
from moderation_actions import *
from role_management import *
from chat_activity_monitoring import *
from logging import *
from machine_learning import *
from integration import *
from dashboard import *
from updates_and_bug_fixes import *

# Load predefined rules from data file
with open('../data/predefined_rules.json', 'r') as file:
    predefined_rules = json.load(file)

# Initialize Discord bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command to mute a user
@bot.command()
async def mute(ctx, member: discord.Member):
    await ctx.send(mute_user(member))

# Command to kick a user
@bot.command()
async def kick(ctx, member: discord.Member):
    await ctx.send(kick_user(member))

# Command to ban a user
@bot.command()
async def ban(ctx, member: discord.Member):
    await ctx.send(ban_user(member))

# Command to assign a role to a user
@bot.command()
async def assign_role(ctx, member: discord.Member, role_name: str):
    await ctx.send(assign_user_role(member, role_name))

# Command to remove a role from a user
@bot.command()
async def remove_role(ctx, member: discord.Member, role_name: str):
    await ctx.send(remove_user_role(member, role_name))

# Command to monitor chat activity
@bot.command()
async def monitor_chat(ctx):
    await ctx.send(monitor_chat())

# Command to log moderation action
@bot.command()
async def log_action(ctx, action: str, member: discord.Member):
    await ctx.send(log_moderation_action(action, member))

# Command to update bot
@bot.command()
async def update_bot(ctx):
    await ctx.send(update_bot())

# Command to fix bugs
@bot.command()
async def fix_bugs(ctx):
    await ctx.send(fix_bugs())

# Start the bot
bot.run('your_token_here') # Replace 'your_token_here' with your bot token