import ollama
import logging
import telebot


list = ''


models_INT= len(ollama.list()['models'])
uModel = ollama.list()['models'][0]['name']
for i in range(0, models_INT):
   list = list + '\n' + str(i + 1) + '.' +  ollama.list()['models'][i]['name']

model_options = {

}

for i in range(0, models_INT):
    model_options['/' + ollama.list()['models'][i]['name']] = ollama.list()['models'][i]['name']
print(model_options)


logger = logging.getLogger(__name__)
logging.basicConfig(filename='OllamaBotLogs.log', filemode='w', level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

bot = telebot.TeleBot("your token here")
    
    
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'this is an ai assistant\n just type something to get answers with AI!')
    logger.info('someone started the bot\n')
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '/list_models: list avalable models\n/"modelname": set the model to use\n/model: see what model you are using\n')
    logger.info('someone asked for help!\n')
    
@bot.message_handler(commands=['list_models'])
def list_models(message):
        bot.reply_to(message, list)
        logger.info('someone listed models!\n')

@bot.message_handler(commands=['qwen:0.5b', 'gemma:2b', 'gemma:7b', 'gemma2:9b'])
def set_model(message):
    global uModel
    uModel = model_options[message.text]
    bot.reply_to(message, f"Model set to {uModel}")
    logger.info('someone changed model to "{uModel}"\n')


@bot.message_handler(commands=['model'])
def model(message):
     bot.reply_to(message, f"Your current model is {uModel}")
     logger.info('someone chacked the current model\n')

@bot.message_handler(func=lambda message: True)
def ask(message):
    question = message.text
    logger.info('someone asked: "{question}" from model: "{uModel}"')
    response = ollama.chat(model=uModel, messages=[
        {
        'role': 'user',
        'content': question,},
        ])
    logger.info(f'"{uModel}" answered to someone question\n')
    bot.reply_to(message, response['message']['content'])

bot.infinity_polling()
