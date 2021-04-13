# TeleNex

TeleNex - это Frimework для простого создания асинхронных Telegram ботов

# Использование

```python
from teleNex import Bot

bot = Bot('<your bot token>')

@bot.on_message(cmds=['start'])
def start(msg):
  bot.send_msg(msg.chat.id, 'Привет, привет!')
  
bot.run()
```
