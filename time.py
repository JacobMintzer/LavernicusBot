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

file_object=open("key.txt","r")
bot.run(file_object.read())