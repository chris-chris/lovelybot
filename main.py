from microsoftbotframework import MsBot
from tasks import echo_response
import os

bot = MsBot(port=int(os.environ['PORT']))
bot.add_process(echo_response)
bot.run()