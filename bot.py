# ---------------------------------------------
token = "INSERT YOUR TOKEN HERE"
correct_chat_id = "INSERT YOUR CHAT ID HERE"

from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, filters
import os, subprocess
# ------------------ FUNCTIONS ------------------
def run_shell_command(command):
  result = subprocess.run(command, shell=True, capture_output=True,
text=True)
  return result.stdout

# --------------------- CODE --------------------

def echo(update: Update, context) -> None:
    message = update.message
    reply = None
    # ------------------ Predefined Responses ------------------
    if message.text == "Test 1":
      reply = "Success 1"
    # ----------------------------------------------------------
    bot = context.bot
    if reply != None:
      try:
        bot.send_message(chat_id=correct_chat_id, text=reply)
      except:
        bot.send_message(chat_id=correct_chat_id, text="⚠️ An error
occured ⚠️")


if __name__ == "__main__":
    bot_token = token

    bot = Bot(token=bot_token)
    updater = Updater(bot=bot)
    dispatcher = updater.dispatcher
    echo_handler = MessageHandler(filters.Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()
