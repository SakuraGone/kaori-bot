import discord
from discord.ext import commands
import re
import random


class Dice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('\tdice loaded.')

    # Commands
    @commands.command()
    async def roll(self, ctx, *args):
        # Check if argument exists
        # Check for format
        if len(args) != 0 and re.fullmatch(r'(\d+(d\d+)?)((?=\+)\+(\d+(d\d+)?))*', args[0]):
            arg_list = args[0].split('+')
            result = 0
            for each in arg_list:
                result += calc_section(each)
            await ctx.send(result)
        else:
            await ctx.send('||Misaka 是狗!||')


# Calculate result for each section
def calc_section(section) -> int:
    if 'd' in section:
        d = section.split('d')
        result = 0
        # Generate random number
        for _ in range(int(d[1])):
            result += random.randint(0, int(d[0]))
        return result
    else:
        return int(section)


def setup(bot):
    bot.add_cog(Dice(bot))
