# meta developer: @mekbect
# meta pic: https://img.icons8.com/emoji/344/grapes-emoji.png
import random

async def choice(self, message):
    choice2 = random.choice(f'Успешно {message}!', f'Не успешно {message}!')
    msg.edit(choice2)
    
