"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from microsoftbotframework import MsBot
from tasks import echo_response

if __name__ == '__main__':
    # HOST = environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555

    bot = MsBot()
    bot.add_process(echo_response)
    bot.run()
