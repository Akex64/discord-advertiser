import discord

client = discord.Client()

message = ''

@client.event
async def on_connect():
	global message
	for guild in client.guilds:
		for guser in guild.members:
			if guser != client.user:
				try:
					user = client.get_user(guser.id)
					dm = await user.create_dm()
					await dm.send(message)
					print(f'Sent messages to {guser.name}#{guser.discriminator}') # ({type(user)})
				except:
					print(f'DMs are disabled for {guser.name}#{guser.discriminator}')

token = input('Token: ')
message = input('Message (Advertisement Text): ')
client.run(token, bot=False)
