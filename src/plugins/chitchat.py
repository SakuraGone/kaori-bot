import discord
from discord.ext import commands
from discord.ext.commands import bot


class Chitchat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('\tchitchat loaded.')

    # Commands
    @commands.command()
    async def hello(self, ctx):
        name = str(ctx.author.name)
        discriminator = str(ctx.author.discriminator)
        # check if the author is calling this command
        if name == 'SakuraGone' and discriminator == '2000':
            await ctx.send('妈妈好~')
        else:
            await ctx.send(f'你好呀~{name}')


def setup(bot):
    bot.add_cog(Chitchat(bot))
