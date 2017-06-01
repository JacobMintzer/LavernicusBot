import discord
from discord.ext import commands
import asyncio
import re
import random
bot = commands.Bot(command_prefix=['!'], description='did you say blood mage?')
@bot.event
@asyncio.coroutine 
def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	yield from bot.change_presence(game=discord.Game(name="with time"))
#	discord.opus.load_opus('opus')
@bot.event
@asyncio.coroutine 
def on_message(message):
	if message.author == bot.user:
		return 0
	if 'blood ma' in message.content.lower() or 'bloodma' in message.content.lower():
		yield from bot.send_message(message.channel,'did someone say blood mage?')
		yield from bot.change_presence(game=discord.Game(type=1,name="bullying blood mages",url='https://www.twitch.tv/pokespeedrunbots'))
	else:
		yield from bot.change_presence(game=discord.Game(name="with time"))
		
	if len(message.content)>3:
		if message.content[0]=='!' and message.content[1].isdigit() and message.content[2]=='d':
		
			if len(message.content)>15:
				yield from bot.send_message(message.channel,'fuck you')
				return 0
			
			n=int(message.content[1])
			#string s
			s=''
			i=3
			each=0
			mod=0
			best=-1
			while i<len(message.content) and message.content[i].isdigit():
				s+=message.content[i]
				i+=1
			if i<len(message.content):
				if message.content[i]=='+':
					mods=''
					i+=1
					while i<len(message.content) and message.content[i].isdigit():
						mods+=message.content[i]
						i+=1
					mod=int(mods)
				if message.content[i]=='-':
					mods=''
					i+=1
					while i<len(message.content) and message.content[i].isdigit():
						mods+=message.content[i]
						i+=1
					mod=-1*int(mods)
			if i<len(message.content):
				if message.content[i]=='e':
					each=1
					i+=1
			if i<len(message.content):
				if message.content[i]=='b':
					best=int(message.content[i+1])
				
			d=int(s)
			i=0
			results=[]
			while i<n:
				if mod!=0:
					if each==1:
						results.append(random.randrange(1,d+1)+mod)
					else:
						results.append(random.randrange(1,d+1))
				else:
					results.append(random.randrange(1,d+1))
				
				i+=1
			i=0
			sum=0
			if best>0:
				sorted(results,reverse=True)
				n=best
			output='```'
			for i in range(0,n):
				output+=str(results[i])
				output+=' '
				sum+=results[i]
			
			if(each==0):
				sum+=mod
			if best==-1:
				output+='\n{0}'.format(message.author)+': total sum: '+str(sum)
			else:
				output+='\n{0}'.format(message.author)+': best '+best+' sum: '+str(sum)
			output+='```'
			yield from bot.send_message(message.channel,output)
		else:
			yield from bot.process_commands(message)
	else:
		yield from bot.process_commands(message)
@bot.event
@asyncio.coroutine 
def on_member_join(member):
	if format(member.server)=='Lavernicus Channel':
		yield from bot.send_message(member.server, 'The legend has come true, Yev has joined the server')
'''		
@bot.command()
@asyncio.coroutine 
def hss(*, stuff_for_snek_to_say):
	"""says stuff"""
	yield from bot.say(stuff_for_snek_to_say)
	
@bot.command()
@asyncio.coroutine
def tiddies():
	"""dem sweet snek tiddies"""
	yield from bot.say('http://i.imgur.com/n3XYGyI.png')
@bot.command()
@asyncio.coroutine 
def pls():
	"""try it"""
	yield from bot.say(':snake:')
@bot.command()
@asyncio.coroutine 
def plsno():
	"""pls no this is a bad idea u will regret it"""
	yield from bot.say('snek pls')
	
@bot.command()
@asyncio.coroutine 
def hello():
	"""hi"""
	yield from bot.say('hello yes this is snek.')
@bot.command()
@asyncio.coroutine 
def hi():
	"""hello"""
	yield from bot.say('hi yes this is snek.')
@bot.command()
@asyncio.coroutine 
def intensifies():
	"""[SNEK INTENSIFIES]"""
	yield from bot.say('http://i.imgur.com/hSZfCiD.gif')
@bot.command()
@asyncio.coroutine 
def noboop():
	"""noboop snek"""
	yield from bot.say('http://i.imgur.com/j4p70OX.jpg')
@bot.command()
@asyncio.coroutine 
def step():
	"""no step on snek"""
	yield from bot.say('http://i.imgur.com/SSkvSQL.jpg')
@bot.command()
@asyncio.coroutine 
def nervous():
	"""nervous hissing"""
	yield from bot.say('http://i.imgur.com/b6s9WTJ.gif')
@bot.command()
@asyncio.coroutine 
def art():
	"""jacob's beautiful art"""
	yield from bot.say (random.choice(['https://farm2.staticflickr.com/1622/24885440680_02487a7356_o_d.gif' , 'https://farm6.staticflickr.com/5700/23833016945_7cab5c3e92_o_d.png']))
@bot.command()
@asyncio.coroutine 
def smug():
	"""u srs askin snek what smug is?"""
	yield from bot.say ('http://orig09.deviantart.net/6e2f/f/2010/132/d/7/5th_gen_starter___tsutaaja_by_arkeis_pokemon.png')
	
@bot.command()
@asyncio.coroutine 
def play(*, game_to_play):
	"""snek likes playing game"""
	yield from bot.change_presence(game=discord.Game(name=game_to_play))
	
@bot.command()
@asyncio.coroutine 
def stream(*, game_to_play):
	"""snek likes streaming game"""
	#yield from bot.change_presence(game=discord.Game(name=game_to_play))
	yield from bot.change_presence(game=discord.Game(type=1,name=game_to_play,url='https://www.twitch.tv/pokespeedrunbots'))
	
@bot.command()
@asyncio.coroutine 
def ily():
	"""tell snek ily"""
	yield from bot.say('snek loves yogurt 2')
@bot.command()
@asyncio.coroutine 
def whoBully():
	"""who does snek bully? (not implemented)"""
	
@bot.command()
@asyncio.coroutine 
def bully(member : discord.User = bot.user):
	"""watch out, snek will bully u"""
	bully_reply=[]
	bully_object=open("bully.txt","r")
	while 1:
		line = bully_object.readline()
		if not line:
			break	
		else:
			bully_reply.append(line)
	yield from bot.say(random.choice(bully_reply).format(member))
@bot.command()
@asyncio.coroutine 
def flirt():
	"""snek is smuuth"""
	flirt_reply=[]
	flirt_object=open("flirt.txt","r")
	while 1:
		line = flirt_object.readline()
		if not line:
			break	
		else:
			flirt_reply.append(line)
	yield from bot.say(random.choice(flirt_reply))
	
@bot.command()
@asyncio.coroutine 
def ifbully():
	"""to bully or not to bully"""
	yield from bot.say (random.choice(['http://i.imgur.com/NRMo4jZ.jpg' , 'http://i.imgur.com/7NEWEFu.jpg']))
@bot.command()
@asyncio.coroutine	
def live():
	yield from bot.say ('i have risen my son')
@bot.command()
@asyncio.coroutine 
def REE():
	"""REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"""
	yield from bot.say('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
	
@bot.command()
@asyncio.coroutine 
def tendies():
	"""snek wants tendies"""
	yield from bot.say('MOM WHERE ARE MY TENDIES\nREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
	
@bot.command()
@asyncio.coroutine 
def sad():
	"""snek is sad"""
	yield from bot.say('https://cdn.drawception.com/images/panels/2012/3-31/8SMj5httsM-12.png')
	
@bot.command()
@asyncio.coroutine 
def whomade():
	"""who made snek?"""
	yield from bot.say('jacob made snekbot2 which was based off of SplitPixl\'s snekbot')
@bot.command()
@asyncio.coroutine 
def info():
	"""info about snekbot"""
	yield from bot.say('snekbot was coded in python with the library discord.py. hss.')
@bot.command()
@asyncio.coroutine 
def invite():
	"""snekbot invite link"""
	yield from bot.say('to add snekbot to your server click this: https://goo.gl/xqfKWn')
@bot.command()
@asyncio.coroutine 
def git():
	"""snek's source code"""
	yield from bot.say('https://github.com/JacobMintzer/snekbot')
'''
file_object=open("key.txt","r")
bot.run(file_object.read())