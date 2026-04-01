import discord
from discord import app_commands
import random
#os : 파일 경로를 다루게 도와줌
import os
from data import survivors

#봇 기본 세팅
class MyBot(discord.Client):
    def __init__(self):
        #인텐트 설정
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        try:
            #안돌아가길래 그냥 디코 서버 아이디 지정 형식으로 했는데.. 수정 필요
            guild = discord.Object(id=1382834320343040101)
            
            # 명령어 동기화 (구동 방식 이해 못함. 추후 공부 필요)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            
            print(f"[{guild.id}] 서버에 명령어 {len(synced)}개 동기화 완료")
        except Exception as e:
            print(e)

bot = MyBot()

#1. 생존자 추첨
@bot.tree.command(name="생존자추첨", description="랜덤으로 생존자를 추첨합니다.")
async def survivor_draw(interaction: discord.Interaction):
    number = random.randint(1, 51)
    
    character_file_name = survivors.get(number, "알 수 없는 캐릭터")
    
    file_name = f"{character_file_name}.jpg"
    
    img_folder = r"D:\discordBot\생추봇_ver1\생존자Img"
    img_path = os.path.join(img_folder, file_name)
    
    #이미지
    if os.path.exists(img_path):
        file = discord.File(img_path, filename="result.jpg") 
        await interaction.response.send_message(
            content=f"🎲 생존자 추첨 결과: **{character_file_name}** 입니다!",
            file=file
        )
    else:
        await interaction.response.send_message(
            content=f"🎲 생존자 추첨 결과: **{character_file_name}** 입니다!\n(이미지를 찾을 수 없습니다: {file_name})"
        )

#2. 감시자 추첨
@bot.tree.command(name="감시자추첨", description="랜덤으로 감시자를 추첨합니다.")
async def hunter_draw(interaction: discord.Interaction):
    number = random.randint(1, 34)
    await interaction.response.send_message(f"👁️ 감시자 추첨 결과: **{number}**번 입니다!")

#실행
bot.run('#')