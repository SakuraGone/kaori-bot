import discord
from discord.ext import commands
from discord.ext.commands import bot


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('\tmusic loaded.')

    # Commands
    @commands.command()
    async def play(self, ctx, url: str):
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="常规")
        voice = discord.utils.get(discord.client.voice_clients, guild=ctx.guild)
        await voiceChannel.connect()


def setup(bot):
    bot.add_cog(Music(bot))
