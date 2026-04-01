#디스코드 임포트
import discord

# Client 클래스 생성
# discord 파일 내 Client 라는 기본 기능을 가져온 후 내 입맛대로 수정하겠다는 이야기
class Client(discord.Client):
		# async : 비동기 처리 : 한줄 한줄 끝나는걸 기다리는게 아닌, 여러 일을 동시에 처리할 준비
		# on_ready : 봇이 서버에 연결되면 할 동작
    async def on_ready(self):
        #봇이 실행될때마다 터비널에 출력 : Logged on as {봇이름}
        print(f"Logged on as {self.user}!")
    # on_message : 서버 사람이 새 채팅을 보낼때마다 자동으로 동작하는 함수
    #  self = 봇 자기 자신, message = 디코 서버 내 발생한 메제시의 모든 정보    
    async def on_message(self, message):
		    # author = 메시지를 보낸 유저는 누구?, content = 그 사람이 보낸 메시지 내용은?
        print(f'Message from {message.author}: {message.content}')


# 권한 설정
# Intents : 봇이 서버에서 무엇을 할지 지정
intents = discord.Intents.default()
# 사람들이 주고받는 메시지 내용을 읽을 권한을 주는것
intents.message_content = True

# 위에서 만든 Class(설계도)를 바탕으로 실제 작동하는 봇 객체를 만드는 과정
Client = Client(intents=intents)
# 
#봇 토큰 입력
Client.run('토큰주소')


