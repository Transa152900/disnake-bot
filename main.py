import disnake
import os
from disnake.ext import commands

client=commands.Bot(command_prefix='TT+', intents=disnake.Intents.all())
client.remove_command( 'help' )

@client.event
async def on_ready():
	print('[LOG] Я запущен!')
	channel = client.get_channel(975256344569450546)
	Embed = disnake.Embed(description = 'Бот запущен!', title = 'Бот запущен', color=0x05fcfa)
	await channel.send(embed=Embed)

@client.command()
async def say(ctx, text, title):
    if ctx.author == 810530800667066369:
        Embed = disnake.Embed(description=text, title=title)
        await ctx.send(embed=Embed)
    else:
        Embed = disnake.Embed(description="Извините но вам нельзя пользоватся командами данного бота.", title="Вы не можете пользоватся этим ботом")
        await ctx.send(embed=Embed) 

@client.event
async def on_member_join(member):
    member = member.name
    Embed = disnake.Embed(description=f'Приветсвую тебя на сервере PressWIN {member}!', title='Привет!')
    channel = client.get_channel(969248263888859156)
    await channel.send(embed=Embed)

@client.event
async def on_member_remove(member):
    member = member.name
    Embed = disnake.Embed(description=f'Пока {member}(', title='Пока(')
    channel = client.get_channel(969248264874504222)
    await channel.send(embed=Embed)

client.run(os.environ["DISCORD_TOKEN"])
