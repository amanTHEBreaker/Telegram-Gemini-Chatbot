import telebot

import google.generativeai as genai
my_api_key_gemini = "GEMINI-API-KEY"
genai.configure(api_key=my_api_key_gemini)
model = genai.GenerativeModel('gemini-pro')

bot = telebot.TeleBot("TELEGRAM-BOT-API-TOKEN", parse_mode="HTML")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Just Ask me anything and I would like to help")

generation_config = {
  "max_output_tokens": 500,
}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = model.generate_content(message.text,generation_config=generation_config)
    bot.reply_to(message, response.text)

bot.infinity_polling()