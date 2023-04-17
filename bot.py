import discord
from discord.ext import commands
import os
import youtube_dl
import random
import threading
import asyncio
import signal
import mutagen
from mutagen.mp3 import MP3
import time

file_check = ["song.mp3"]

client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")




# if this mess up within multiple servers, it's because this function is synchronous (prob)
def dl_video(url, names):
    # can specify 'outtpml' if music should be saved elsewhere, but then you'd have to
    # manipulate the "play" directory in the commands themselves
    x = names
    ydl_opts = {
        'format': 'bestaudio/best',
        'title': x,
        'outtmpl': "song.mp3",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:    
        ydl.download([url])

               


@client.event
async def on_ready():
    #kofu = await client.fetch_user(324268216321048576)
    #await kofu.send("I'm ready!")

    print("running!")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.isfile("victory.mp3"):

        dl_video("https://youtu.be/bY42td07WBs", "victory.mp3")

@client.command()
async def play(ctx, url):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")

    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return


    dl_video(url, "song.mp3")

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("song.mp3"))
    print("playing song")


@client.command()
async def stop(ctx):
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("Not in a voice channel!")

@client.command()
async def pause(ctx):
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.pause()
    else:
        await ctx.send("Not playing anything!")

@client.command()
async def resume(ctx):
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice_client.is_paused():
        voice_client.resume()
    else:
        await ctx.send("Not playing anything!")

@client.command()
async def victoryroyale(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")

    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("victory.mp3"))
    print("playing victory royale")


@client.command()
async def top10(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")

    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("top101.mp3"))
    print("playing top10")


@client.command()
async def jason(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("jason.wav"))
    print("playing jason")



@client.command()
async def gachi(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    songs = os.listdir("./gachi")
    song = "./gachi/" + random.choice(songs)

    voice_client.play(discord.FFmpegPCMAudio(song))
    
    print("playing gachi")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def aris(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    songs = os.listdir("./aris")
    song = "./aris/" + random.choice(songs)

    voice_client.play(discord.FFmpegPCMAudio(song))
    
    print("playing aris")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()
    

@client.command()
async def cumming(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("cummin.mp3"))
    print("playing cummin")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()    

    

@client.command()
async def dancingallnight(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    songs = os.listdir("./persona")
    song = "./persona/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing dancin")


@client.command()
async def gamers(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("gamers.mp3"))
    print("playing gamers")



@client.command()
async def awaken(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("awaken.mp3"))
    print("playing awaken")

@client.command()
async def hellohello(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("HELLO_HELLO.wav"))
    print("playing hellohello")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()


@client.command()
async def glowstick(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("I_have_me_glow_stick.wav"))
    print("playing glowstick")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()    

@client.command()
async def bathroom(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("bathroom.mp3"))
    print("playing bathroom")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def combat(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("great_combat.wav"))
    print("playing great combat")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()



@client.command()
async def kage(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("kage.mp3"))
    print("playing kage.mp3")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def dhc(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("dhc.mp3"))
    print("playing dhc.mp3")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()


@client.command()
async def timu(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("timu.mp3"))
    print("playing timu.mp3")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()


@client.command()
async def xgod(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    songs = os.listdir("./xgod")
    song = "./xgod/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing xgod")



@client.command()
async def gsl(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("SEIZE_THE_STAKES.mp3"))
    print("playing SEIZE_THE_STAKES.mp3")

@client.command()
async def mario(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("mario.mp3"))
    print("playing mario.mp3")

@client.command()
async def james(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("jamespain.mp3"))
    print("playing jamespain.mp3")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()




    
@client.command()
async def oblivion(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    songs = os.listdir("./oblivion")
    song = "./oblivion/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing oblivion")




@client.command()
async def biggergun(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    print("playing bigger gun.mp3")

    songs = os.listdir("./biggergun")
    song = "./biggergun/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing biggergun")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def captain(ctx, *name):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    print("playing captain.mp3")
    songs = os.listdir("./who")
    strr = ''.join(name)

    if (strr != ""):
        song = "./who/" + strr + ".mp3"
    else:
        song = "./who/" + random.choice(songs)
           
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing captain")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect() 


@client.command()
async def chaos(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    print("playing chaos.mp3")

    songs = os.listdir("./chaos")
    song = "./chaos/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing chaos")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()


        
@client.command()
async def artosis(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./art")
    song = "./art/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing art")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def ayaya(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./ayaya")
    song = "./ayaya/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing ayaya")
    
@client.command()
async def reyn(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./reyn")
    song = "./reyn/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing reyn")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def shenmue(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./shenmue")
    song = "./shenmue/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing shenmue")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def hahaha(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./hahaha")
    song = "./hahaha/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing hahaha")
    
  
@client.command()
async def starcraft(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./starcraft")
    song = "./starcraft/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing starcraft")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()




@client.command()
async def blacktar(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    voice_client.play(discord.FFmpegPCMAudio("blacktar.mp3"))
    print("playing blacktar.mp3")


@client.command()
async def funny(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./funny")
    song = "./funny/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing funny")
    
@client.command()
async def mason(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./mason")
    song = "./mason/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing mason")

    
@client.command()
async def weareelectric(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("We Are Electric.mp3"))
    print("WE ARE ELECTRIC")



@client.command()
async def sundowner(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    songs = os.listdir("./sundowner")
    song = "./sundowner/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing sundowner")
    
    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def libertarian(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("libertarian.mp3"))
    print("TOASTER LICENSE?")

@client.command()
async def yugioh(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("yugi.mp3"))
    print("yuhioh?")


@client.command()
async def kotl(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("kotl.mpeg"))
    print("kotl?")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def hamburger(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("hamburger.mp3"))
    print("hamn?")

    while voice_client.is_playing():
        pass
    if voice_client.is_connected():
        await voice_client.disconnect()

@client.command()
async def zato1(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("numberoneinrainworld.mp3"))
    print("numberoneinrainworld?")

@client.command()
async def internets(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)


    voice_client.play(discord.FFmpegPCMAudio("internets.mp3"))
    print("internets?")

@client.command()
async def crts(ctx):
    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")


    except PermissionError:
        await ctx.send("Can't play song, there's already one playing!")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    songs = os.listdir("./crt")
    song = "./crt/" + random.choice(songs)
    voice_client.play(discord.FFmpegPCMAudio(song))
    print("playing crt")







# here's some code directly stolen from our lord and savior rapptz, worth looking at

"""@commands.command()
async def stream(self, ctx, *, url):
    # Streams from a url (same as yt, but doesn't predownload)
    player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('Now playing: {}'.format(player.title))"""



client.run("ODIyOTUwMzAyMjIyOTA5NDUw.YFZuMQ.qyv4nl8ImjP6kLcbLqMRzKKNJ1k")
