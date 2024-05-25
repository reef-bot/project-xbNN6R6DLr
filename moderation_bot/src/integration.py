# integration.py

import discord
from discord.ext import commands
import moderation_actions
import role_management
import chat_activity_monitoring
import logging

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    await moderation_actions.mute_member(ctx, member)

@bot.command(name='kick')
async def kick(ctx, member: discord.Member):
    await moderation_actions.kick_member(ctx, member)

@bot.command(name='ban')
async def ban(ctx, member: discord.Member):
    await moderation_actions.ban_member(ctx, member)

@bot.command(name='assign_role')
async def assign_role(ctx, member: discord.Member, role: discord.Role):
    await role_management.assign_role(ctx, member, role)

@bot.command(name='remove_role')
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    await role_management.remove_role(ctx, member, role)

@bot.event
async def on_message(message):
    await chat_activity_monitoring.monitor_message(message)

@bot.event
async def on_member_join(member):
    await logging.log_member_join(member)

@bot.event
async def on_member_remove(member):
    await logging.log_member_remove(member)

bot.run('YOUR_DISCORD_TOKEN')