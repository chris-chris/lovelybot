from microsoftbotframework import MsBot
from tasks import echo_response

bot = MsBot()
bot.add_process(echo_response)
bot.run()