# Ollama-telegram-bot
a telegram bot for telegram

options:<br/>
`list avalable models`<br/>
`change the models`<br/>
`tell what model you are using`<br/>

not avalable stuff:
`automatic model listing`

a log file named **OllamaBotLogs.log** will be created next to the **app.py** to show logs to the bot owner. it shows:<br/>
_when someone started the bot_<br/>
_what model did someone aks from_<br/>
_what command did someone use_<br/>

it doesn't show:<br/>
_who did those things_<br/>

installation:<br/>
1.install [python](https://python.org)

2.install [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI?tab=readme-ov-file#writing-your-first-bot): 
`pip install pyTelegramBotAPI` (go to its github page if you cant use **pip**)<br/>

3.download the latest version from releses part of this page<br/>

4.make a bot in [botfother](https://t.me/BotFather) (start by typing **/newbot** and the do what it tells you)<br/>

5.replace the word **token** in line 19 with the token that you got from botfather<br/>

6.put the list of models you have installed with ollama in the `model_options` at line 8 like the example<br/>

7.change the `list` in line 7 variable according to your needs<br/>

8.open terminal and cd to the folder you put the _app.py_ in: `cd PATH/TO/APP.PY`<br/>

9.start the bot: run `python3 app.py` or `python app.py` in terminal<br/>

(optional)<br/>
run `python3 app.py &` or `python app.py &` to run the bot in background (linux)<br/>
add `python3 app.py &` or `python app.py &` to your startup apps for easy access after boot<br/>




