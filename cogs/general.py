from   discord.ext import commands
import discord

from   random      import choice
import random


"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.
For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class General(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='react', aliases=['emote', 'emoji'])
    async def do_react(ctx):
        def check(r, u):
            return u == ctx.message.author and r.message.channel == ctx.message.channel and str(r.emoji) == '✅'

        await ctx.send("React to this with ✅")
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=300.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Timeout')
        else:
            await ctx.send('Cool, thanks!')
        
    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        """The one, the only, copycat command"""

        await ctx.send(our_input)

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='info')
    @commands.guild_only()
    async def info_command(self, ctx):
        """ displays information about the bot """
        embed = discord.Embed(title='\nSummary',
                              description='Ghento is designed to be as entertaining as possible resulting\nin the best experince on your discord server ',
                              colour=0x98FB98)
        embed.set_author(name='Ghento Bot Information',
                         url='https://discordapp.com/api/oauth2/authorize?client_id=616092750051409928&permissions=8&scope=bot',
                         icon_url='https://cdn.discordapp.com/attachments/615011904410222595/616109163315200020/istockphoto-673647420-612x612.jpg')

        embed.add_field(name='Server Invite', value='[Invite to server](https://discordapp.com/api/oauth2/authorize?client_id=616092750051409928&permissions=8&scope=bot)')
        embed.add_field(name='Invoked By', value=ctx.author.mention)
        embed.set_footer(text='\nMade in Python', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(embed=embed)

    @commands.command()
    async def flip(self, ctx, user: discord.Member = None):
        """Flip a coin... or a user.
        Defaults to a coin.
        """
        faces = ['Heads!**_', 'Tails!**_']
        if user is not None:
            msg = ""
            if user.id == ctx.bot.user.id:
                user = ctx.author
                msg = "Nice try. You think this is funny?\n How about *this* instead:\n\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await ctx.send(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await ctx.send('_You got... **'+random.choice(faces))

    @commands.command()
    @commands.guild_only()
    async def serverinfo(self, ctx):
        """Show server information."""
        guild = ctx.guild
        online = (
            len([m.status for m in guild.members if m.status != discord.Status.offline])
        )
        total_users = str(len(guild.members))
        text_channels = str(len(guild.text_channels))
        voice_channels = str(len(guild.voice_channels))
        passed = (ctx.message.created_at - guild.created_at).days
        created_at = "Since {date}. That's over {num} days ago!".format(
            date=guild.created_at.strftime("%d %b %Y %H:%M"), num=passed
        )
        data = discord.Embed(description=created_at, colour=0x8080ff)
        data.add_field(name="Region", value=str(guild.region), inline=True)
        data.add_field(name="Users", value=f"{online}/{total_users}", inline=False)
        data.add_field(name="Text Channels", value=text_channels, inline=True)
        data.add_field(name="Voice Channels", value=voice_channels, inline=True)
        data.add_field(name="Roles", value=str(len(guild.roles)), inline=True)
        data.add_field(name="Owner", value=guild.owner, inline=True)
        data.set_footer(text="Server ID: " + str(guild.id), inline=True)

        if guild.icon_url:
            data.set_author(name=guild.name, url=guild.icon_url)
            data.set_thumbnail(url=guild.icon_url)
        else:
            data.set_author(name=guild.name)

        try:
            await ctx.send(embed=data)
        except discord.Forbidden:
            await ctx.send("I need the `Embed links` permission to send this.")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild.
        For this example I will keep things simple and just print some info.
        Notice how because we are in a cog class we do not need to use @bot.event
        For more information:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        Check above for a list of events.
        """

        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')
    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = member.server


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(General(bot))
