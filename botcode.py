#Moduals
import discord,os, json, requests
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

#deps
TOKEN = os.getenv("TOKEN")
INTENTS = discord.Intents.default()

#client
client = discord.Client(intents=INTENTS)



async def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a'] 
    return(quote)

#reddy message
@client.event
async def on_ready():
    await client . change_presence(status=discord. Status . idle, activity=discord .Game("check my code here-https://github.com/Null-B/bot " ))
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')




#comands

@commands.Cog.listener()
async def on_member_join(self, member):
    for channel in member.guild.channels:
        if str(channel) == "join-leave":
            embed = discord.Embed(color=0x4a3d9a)
            embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=False)
            embed.set_image(url="https://newgitlab.elaztek.com/NewHorizon-Development/discord-bots/Leha/-/raw/master/res/welcome.gif")
            await channel.send(embed=embed)

    #help
 
    @client.event
    

    #all the text comands
    async def on_message(message):


        if message.content.startswith('$help'):
                embedVar = discord.Embed(title="Comads", description="dont forget to use the \"$\" to use the comands", color=0x00ff00)
                embedVar.add_field(name="Hi comads", value="$hi / $hello / $sup", inline=False)
                await message.channel.send(embed=embedVar)
        

        #hi comands
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!😀')

        if message.content.startswith('$hi'):
            await message.channel.send('eyyyy😀')

        if message.content.startswith('$sup'):
            await message.channel.send('sup my dued😀')
        
        #inspiration 
        if message.content.startswith('$inspire'):
            quote = get_quote() 
            await message.channel.send(quote) 

client.run(TOKEN)