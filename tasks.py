from microsoftbotframework import ReplyToActivity

def echo_response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=message["text"]).send()
