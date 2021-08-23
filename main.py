import discord
from datetime import date
current_date = date.today()
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())
bot.remove_command("help") #Удаляем команду help


@bot.event  # сообщение подключение
async def on_ready():

    print("Подключился к серверу!")
    #current_time = datetime.now().time()
    print("Был запущен -",current_date)


@bot.command()  # отправка сообщения в лс
async def send_m(ctx, member: discord.Member):
    await member.send(f"{member.name},Проверка на бота от  {ctx.author.name},отправь + в канал помощь")
    await ctx.channel.purge(limit=1)


@bot.event  # Приветсвие и выдоча роли пользователю
async def on_member_join(member):
    channelsadg = bot.get_channel(876388189579911168)  # Id канала приветсвия
    role = discord.utils.get(member.guild.roles, id=876392749912444958)
    await member.add_roles(role)
    await channelsadg.send(f' {member.mention} У нас новый выживший! если нужна помощь (!help) ')


# async def send_m(ctx,member: discord.member)

@bot.event  # Проощяние с пользователем
async def on_member_remove(member):
    channelsadg = bot.get_channel(876388189579911168)  # Id канала
    await channelsadg.send(f'Увы {member.mention} покинул нас')


@bot.command()  # Рассылка message_all
@commands.has_permissions(administrator=True)  # права на команду
async def message_all(ctx):
    file = open("D:\BotTEST\Rassilka.txt", encoding="utf8")
    content = file.read()
    file.close()
    for guild in bot.guilds:
        for member in guild.members:
            await member.send(content)

            print("Отправил " + str(member))


@bot.command(pass_context=True)  # очистка !clear
@commands.has_permissions(administrator=True)  # права на команду
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Очищено - {amount} - сообщений ")


@bot.command(pass_context=True)  # команда help
#@commands.has_permissions(administrator=True)
async def help(ctx):
    file = open("D:\BotTEST\helpnavigateons.txt", encoding="utf8")
    content = file.read()
    file.close()
    await ctx.send(content)

@bot.command()
async def rules(ctx): #правила
    file = open("D:\BotTEST\Rules.txt", encoding="utf8")
    content = file.read()
    file.close()
    await ctx.send(content)

@bot.command()
async def info(ctx):#информация
    file = open("D:\BotTEST\Info.txt", encoding="utf8")
    content = file.read()
    file.close()
    await ctx.send(content)

@bot.command()
async def verification(ctx): #верефикация
    file = open("D:\BotTEST\Verification.txt", encoding="utf8")
    content = file.read()
    file.close()
    await ctx.send(content)

@bot.event
async def on_command_error(ctx, error): #ошибка при вводе команды
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует! Есле нужна помощь !help.**', color=0x0c0c0c))

@bot.event # Лог удаления сообщения
async def on_message_delete(message):
    file = open("D:\BotTEST\messages\messagesLOG.txt", "a")
    file.write(f"\n Сообщение было удалено! -> {message.content} \n автор - {message.author} было удалено в {message.channel.id} \n Время - {current_date} \n")
    file.close()
    print(f'Сообщение было удалено! -> {message.content} автор - {message.author} было удалено в {message.channel} \n Время - {current_date}')
    channelsadg = bot.get_channel(876392219425275965)  # Id канала LOG
    await channelsadg.send(f'``` Сообщение было удалено! -> {message.content} \n автор - {message.author} было удалено в {message.channel} \n Время - {current_date} ``` ')


@bot.event #Лог измененых сообщений
async def on_message_edit(before, after):
    file = open("D:\BotTEST\messages\messagesLOG.txt", "a")
    file.write(f" \n Сообщение было изменено! \n Было -> {before.content}, стало -> {after.content} \n Автор - {after.author} было изменено в {after.channel.id} \n Время - {current_date} \n")
    file.close()
    print(f"Сообщение было изменено! \n Было -> {before.content}, стало -> {after.content} \n Автор - {after.author} было изменено в {after.channel} \n Время - {current_date} ")
    channelsadg = bot.get_channel(876392219425275965)  # Id канала LOG
    await channelsadg.send(f"``` Сообщение было изменено! \n Было -> {before.content}, стало -> {after.content} \n Автор - {after.author} было изменено в {after.channel} \n Время - {current_date} ``` " )





bot.run(settings['token'])


