import discord
from discord import app_commands
import random
from discord.ext import tasks
from discord.ext import commands
import datetime
import asyncio
import sys
import time

MY_GUILD = discord.Object(id=890466752960552960)
class MyClient(discord.Client):
    def __init__(self,*,intents:discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intent = discord.Intents.default()
intent.message_content = True
client = MyClient(intents=intent)

mon1 =("言語文化","数学A","家庭基礎","家庭基礎","音/美","体育","英語C 1")
tus1 =("音/美","数1・2","言語文化","英語C 1","物理基礎","地理総合","論表現1")
wed1 =("数1・2","歴史総合","言語文化","論表現1","LHR","総合探求")
thu1 =("体育","生物基礎","数学A","数1・2","保険","英語C 1","論表現1")
fri1 =("数学A","生物基礎","現代国語","地理総合","英語C 1","数1・2","歴史総合")
sut1 =("物理基礎","英語C1・SE","数1・2","現代国語")

mon2 = ("生物基礎","数1・2","家庭基礎","家庭基礎","数学A","体育","論表現1")
tus2 = ("数学A","音/美","言語文化","数1・2","論表現","地理総合","英語C 1")
wed2 = ("現代国語","歴史総合","生物基礎","数学A","LHR","総合探求")
thu2 = ("体育","言語文化","地理総合","音/美","保険","英語C 1","数1・2")
fri2 = ("歴史総合","物理基礎","現代国語","英語C 1","言語文化","論表現1","生物基礎")

token = "MTA3NjQ2NzY3NTgyNTQ1NTE0NQ.GdTwdz.5gicVugMjZaWXjNxunk22pLS5f9Sb1UEv8lqQ4"

@client.event
async def on_ready():
    #loop.start()
    print("起動しました。")
@client.event
async def on_message(message):
    if message.content.startswith("test"):#test
        await message.channel.send("ok")

    if message.content.startswith("exit"):#finish command
        await message.channel.send("終了します")
        sys.exit()


taskes_list = []
@client.tree.command(
        name = "takes",
        description = "タスク管理"
)
@app_commands.describe(making_taskes= "タスクを入力してね")
async def ctimer(inter:discord.Interaction,making_taskes:str):
    try:
        await inter.response.defer()
        taskes_list.append(making_taskes)
        await inter.followup.send("リストに追加できたよ")
    except:
        await inter.followup.send("知らんが問題起きた。")
        pass
@client.tree.command(
        name = "open_takes",
        description = "タスク調査"
)
@app_commands.describe(open_list= "タスクを網羅するよ")
async def ctimer(inter:discord.Interaction,open_list:str):
    await inter.response.defer()
    for taskes_list_variation in taskes_list:
        taskes_list_variation = taskes_list_variation 
    if open_list == "open":
        embeds=discord.Embed(title="taskes",description="", color=0x000000)
        embeds.add_field(name="task_list", value=taskes_list_variation,inline = True)
        await inter.followup.send(embed=embeds)
    if open_list == "open_times":
        await inter.followup.send("現在開拓中")


@client.tree.command(
        name = "timer",
        description = "タイマーを設定できます。"
)
@app_commands.describe(set_times = "半角の数字だけ入力してね。")
async def ctimer(inter:discord.Interaction,set_times:int):
#    if message.content.startswith("c_t"):#sleep comand
        try:
            await inter.response.defer()
            await inter.followup.send(f"{set_times}分のタイマーを設定しました。{inter.user.mention}")
            fintime = int(time.time()) + int(set_times)
            
            now = datetime.datetime.now()
            micro = datetime.timedelta(microseconds=now.microsecond)
            next = datetime.timedelta(minutes=int(set_times))
            #next = now.strftime(f'%d日%:'+())
            #print(next)
            finish_time = now+next-micro

            embeds=discord.Embed(title="タイマー",description="", color=0x000000)
            embeds.add_field(name="設定タイム", value=(f"設定時間:{set_times}分\n終了時刻:{finish_time}"),inline = True)
            embeds.set_footer(text=str(datetime.datetime.now().strftime('%Y.%m.%d, %H:%M:%S')))
            msg = await client.get_channel(inter.channel.id).send(embed=embeds)
            await asyncio.sleep(int(set_times) * 60)

            t6_set = int(time.time()) + int(set_times)
            await inter.channel.send(f"タイムアップ！{inter.user.mention}")
            pass
        except TimeoutError:
            await inter.channel.send("時間切れだよ、もう一回呼んでね")
        except ValueError:
            await inter.channel.send("あれ？文字じゃなくて数字で書いてね")
"""
@client.slash_command()
async def cdebate(msg):  
#    if message.content.startswith("c_d"):
        debate = random.choice(debate_list)
        await msg.respond("title : "+debate)
"""
@client.event
async def today_class(classes):
        message1 = client.get_channel(1079365525899059230)
        await message1.send(classes)
@client.event
async def today_class1(classes):
        message1 = client.get_channel(1079365525899059230)
        await message1.send(classes)
'''
@tasks.loop(hours=1)
async def loop():
    message1 = client.get_channel(1079365525899059230)
    today = datetime.date.today()
    now = datetime.datetime.now().hour
    weekday = int(today.weekday())
    class_point = 0
    if now == 21:
        if class_point == 1:
            if weekday == 6:
                    await today_class1(mon1)
            if weekday == 0:
                    await today_class1(tus1)
            if weekday == 1:
                    await today_class1(wed1)
            if weekday == 2:
#                for main3 in thu1:
                    await today_class1(thu1)
            if weekday == 3:
#                for main4 in fri1:
                    await today_class1(fri1)
            if weekday == 4:
#                for main5 in sut1:
                    await message1.send(sut1)
            if weekday == 5:
                await message1.send("None class")
                class_point = class_point - 1
                embeds=discord.Embed(title="B週の予定",description="今週の予定", color=0x000000)
                embeds.add_field(name="月曜日",value=(mon2),inline = True)
                embeds.add_field(name="火曜日",value=(tus2),inline = True)
                embeds.add_field(name="水曜日",value=(wed2),inline = True)
                embeds.add_field(name="木曜日",value=(thu2),inline = True)
                embeds.add_field(name="金曜日",value=(fri2),inline = True)
                msg = await message1.send(embed=embeds)
        if class_point == 0:
            if weekday == 7:
#                for main in mon2:
                    await today_class(mon2)
            if weekday == 0:
#                for main1 in tus2:
                    await today_class(tus2)
            if weekday == 1:
#                for main2 in wed2:
                    await today_class(wed2)
            if weekday == 2:
#                for main3 in thu2:
                    await today_class(thu2)
            if weekday == 3:
#                for main4 in fri2:
                    await today_class(fri2)
            if weekday == 4:
                await message1.send("None class")
            if weekday == 5:
                await message1.send("None class")
                class_point = class_point + 1
                embeds=discord.Embed(title="A週の予定",description="今週の予定", color=0x000000)
                embeds.add_field(name="月曜日",value=(mon1),inline = True)
                embeds.add_field(name="火曜日",value=(tus1),inline = True)
                embeds.add_field(name="水曜日",value=(wed1),inline = True)
                embeds.add_field(name="木曜日",value=(thu1),inline = True)
                embeds.add_field(name="金曜日",value=(fri1),inline = True)
                embeds.add_field(name="土曜日",value=(sut1),inline = True)
                msg = await message1.send(embed=embeds)
'''


#ニュース
chigyuu_id = "UCTftnkJ6Mkyz5wdX2jozsmw"

#頭脳系
bluebrownJapan_id = "UCBevyiJ2ierZY-0yZhfLrmQ"
scirncemania_id = "UCPXmsBz7MGHcQmyYipFfNdw"
saimon_id = "UCOPQ4nWRjA6BTwPE2hIiPTg"

#音楽系
teto_id = "UCjO8434Ou_9OaeXyOfxjbjA"
yonezu_id = "UCUCeZaZeJbEYAAzvMgrKOPQ"
yayoi_id = "UCzTwIedETJq-dLqAhieCm2A"
nanasi_id = "UCdWCKj9KMLRKub_ocPUtsNQ"


#豆知識や趣味
nozomkubata_id = "UCFhlkeINByW0hGGXoJ0zFiA"
aquastory_id = "UCBWahno6hBisjiqvJVqrkYA"

from googleapiclient.discovery import build
from apiclient import errors

YOUTUBE_API_KEY = "AIzaSyB4ZKPYCq1KyjO9R84u_J1neKY5CPccNMQ"

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

channel_id = saimon_id

def youtube_search(YOUTUBE_API_KEY, channel_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        part='id,snippet',
        channelId=channel_id,
        order='date', # 日付順に並び替え
        type='video', # 動画のみ取得
        maxResults=1 # 5件取得
    )
    
    response = search_response.execute()
    
    videos = ['https://www.youtube.com/watch?v=' + item['id']['videoId'] for item in response['items']]
    print(videos)

    video(videos)
    @client.event
    async def video(video):
        msgch = client.get_channel(1111645320552665108)
        await msgch.send(video)

if __name__ == "__main__":
     youtube_search
client.run(token)