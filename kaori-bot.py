import discord
import os
import config
from discord.ext import commands
from datetime import datetime
from discord import File

# set command prefix
bot = commands.Bot(command_prefix=config.COMMAND_PREFIX)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'src.plugins.{extension}')
    await ctx.send(f'Loaded {extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'src.plugins.{extension}')
    await ctx.send(f'Unloaded {extension}')


@bot.command()
async def reload(ctx, extension):
    await ctx.send(f'Reloading {extension}')
    bot.unload_extension(f'src.plugins.{extension}')
    bot.load_extension(f'src.plugins.{extension}')
    await ctx.send(f'Done {extension}')


# find all .py file in ./src/plugins and load command
for filename in os.listdir('./src/plugins'):
    if filename.endswith('.py'):
        bot.load_extension(f'src.plugins.{filename[:-3]}')


# Print discord real time chat in console
@bot.event
async def on_message(message):
    author = str(message.author.name)+'#'+message.author.discriminator
    # MISAKA#0268

    if message.attachments:
        time = message.author.joined_at.strftime("%m/%d/%Y, %H:%M:%S")
        print('@' + time + ' [' + author + ']: ' + message.attachments[0].url)
    else:
        time = message.author.joined_at.strftime("%m/%d/%Y, %H:%M:%S")
        print('@' + time + ' [' + author + ']: ' + message.content)

    if author == 'MISAKA#0268':
        if message.attachments:
            await message.channel.send('||~~数据删除: [' + message.author.name + ' 上传了文件: ]~~||')
            file = message.attachments[0]
            file.filename = f"SPOILER_{file.filename}"
            spoiler = await file.to_file()
            await message.channel.send(file=spoiler)
        else:
            await message.channel.send('||~~数据删除: [' + message.author.name + ' 说: "' + message.content + '"]~~||')
        await message.delete()

    await bot.process_commands(message)

# never share your bot token
bot.run(config.DISCORD_TOKEN)
