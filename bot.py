import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!d ')

@client.event
async def on_ready() :
    print('Bot is ready')
    
games = []

@client.event
async def on_message(message) :
    sent = message.content
    id = client.get_guild(584013936559521827)
    if message.content.find('ping') != -1 and message.author.name != 'D&D bot':
        await message.channel.send('pong')
    if message.content.find('!d crgame') != -1 and message.author.name != 'D&D bot':
        gname = sent[10:]
        games.append([gname,[],''])
        games[-1][1].append(message.author.name)
        print(games)
        await message.channel.send(gname+' succesfully created')
    if message.content.find('!d end') != -1 and message.author.name != 'D&D bot':
        dgame = sent[7:]
        dpos = -1
        dt = False
        for i in games :
            dpos+=1
            if i[0] == dgame :
                dt = True
                break
        if message.author.name == games[dpos][1][0] :
            if dt == True :
                games.remove(games[dpos])
                await message.channel.send(dgame+' succesfully deleted')
            else :
                await message.channel.send('There is no game named '+dgame)
        else :
            await message.channel.send('Only game creator ('+games[dpos][1][0]+') can delete that game!')
    if message.content.find('!d leave') != -1 and message.author.name != 'D&D bot' :
        lgame = sent[9:]
        lpos = -1
        lt = False
        for i in games :
            lpos+=1
            if i[0] == lgame :
                lt = True
                break
        if lt == False :
            await message.channel.send('There is no game named '+lgame)
        else :
            if message.author.name not in games[lpos][1] :
                await message.channel.send('You are not in that game!')
            elif message.author.name == games[lpos][1][0] :
                await message.channel.send('Creator cannot leave the game!')
            else  :
                games[lpos][1].remove(message.author.name)
                await message.channel.send('You left '+lgame)
    if message.content.find('!d join') != -1 and message.author.name != 'D&D bot':
        jgame = sent[8:]
        jpos = -1
        jt = False
        for i in games :
            jpos+=1
            if i[0] == jgame :
                jt = True
                break
        if jt == False :
            await message.channel.send('There is no game named '+lgame)
        else :
            if message.author.name in games[jpos][1] :
                await message.channel.send('You are already in that game!')
            else  :
                games[jpos][1].append(message.author.name)
                await message.channel.send('You joined '+jgame)
    if message.content.find('!d master') != -1 and message.author.name != 'D&D bot':
        mgame = sent[10:]
        mpos = -1
        mt = False
        for i in games :
            mpos+=1
            if i[0] == mgame :
                mt = True
                break
        if mt == False :
            await message.channel.send('There is no game named '+mgame)
        else :
            if games[mpos][2] == '' :
                mr = random.choice(games[mpos][1])
                games[mpos][2] = mr
                await message.channel.send(mgame+' game master is @'+mr)
            else :
                if message.author.name != games[mpos][2] :
                    await message.channel.send('Only current game master can switch the game master role to another random person!')
                else :
                    mr = random.choice(games[mpos][1])
                    games[mpos][2] = mr
                    await message.channel.send(mgame+' game master is '+mr)
    if message.content.find('!d info') != -1 and message.author.name != 'D&D bot':
        igame = sent[8:]
        ipos = -1
        it = False
        for i in games :
            ipos+=1
            if i[0] == igame :
                it = True
                break
        if it == False :
            await message.channel.send('There is no game named '+igame)
        else :
            await message.channel.send('NAME: '+igame)
            await message.channel.send ('CREATOR: '+games[ipos][1][0])
            await message.channel.send('GAME MASTER: '+games[ipos][2])
            await message.channel.send('PLAYERS: '+str(games[ipos][1])+' '+str(len(games[ipos][1])))
    if message.content.find('!d dice') != -1 and message.author.name != 'D&D bot':
        dice = sent[8:]
        n1,n2 = map(int,dice.split())
        await message.channel.send(random.randint(n1,n2))
    if message.content.find('!d games') != -1 and message.author.name != 'D&D bot':
        alg = ''
        for i in games :
            alg = alg + i[0] + ' '
        if alg == '' :
            await message.channel.send('There are no games available!')
        else :
            await message.channel.send(alg)
    if message.content.find('!d kick') != -1 and message.author.name != 'D&D bot':
        kall = sent[8:]
        kgame,kpe = map(str,kall.split())
        kpos = -1
        kt = False
        for i in games :
            kpos+=1
            if i[0] == kgame :
                kt = True
                break
        if kt == False :
            await message.channel.send('There is no game named '+kgame)
        else :
            if message.author.name != games[kpos][1][0] :
                await message.channel.send('Only game creator can kick players!')
            else :
                if message.author.name == kpe :
                    await message.channel.send('You cannot kick yourself')
                else :
                    if kpe not in games[kpos][1] :
                        await message.channel.send(kpe+' is not in '+kgame)
                    else :
                        games[kpos][1].remove(kpe)
                        await message.channel.send(kpe+' kicked from '+kgame)
    if message.content.find('!d help') != -1 and message.author.name != 'D&D bot':
        await message.channel.send(''' !d crgame <name> -creates a game
!d join <game> -join a game
!d leave <game> -leaves a game
!d kick <game> <player> -kicks a player from the game
!d master <game> -randomly chooses game master
!d info <game>
!d games -lists all available games
!d dice <x> <y> -rolls a dice containing numbers from x to y ''')

client.run('NTg0MDEyMzU5OTU4Mzk2OTQz.XPEuzA.sW1DyEl7sKWXnAKtX3GzDr6i10Q')
