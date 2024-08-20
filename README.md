# Ollama-telegram-bot
a telegram bot for telegram

commads:<br/>
`/list_models`: list available models<br/>
`/"modelName"`: change the model<br/>
`/moedel`: tell what model you are using<br/>
`/help`: list commands<br/>

a log file named **OllamaBotLogs.log** will be created next to the **app.py** to show logs to the bot owner. it shows:<br/>
_when someone started the bot_<br/>
_what model did someone ask from_<br/>
_what command did someone use_<br/>

it doesn't show:<br/>
_who did those things_<br/>

!!you must have [ollama](https://ollama.com) installed for this to work!!<br/>

installation:<br/>
1.install [python](https://python.org)

2.install requirements:  (go to their github page if you cant use **pip**)<br/>
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI?tab=readme-ov-file#writing-your-first-bot): `pip install pyTelegramBotAPI`<br/>
[Ollama Python Library](https://github.com/ollama/ollama-python): `pip install ollama`

3.download the latest version from releses part of this page(dont download `updatechecker.py`) (the one from the files is the oldest version)<br/>

4.make a bot in [botfother](https://t.me/BotFather) (start by typing **/newbot** and the do what it tells you)<br/>

5.replace the word **token** in line 26 (19 on V1.0) with the token that you got from botfather<br/>

6.open terminal and cd to the folder you put the _app.py_ in: `cd PATH/TO/APP.PY`<br/>

7.start the bot: run `python3 app.py` or `python app.py` in terminal<br/>

_only on V1.0:_**(these are NOT optional for V1.0)**

1.put the list of models you have installed with ollama in the `model_options` at line 9 like the example<br/>

5.change the `list` variable in line 7 according to your needs<br/>

3.change the `uModel` variable in line 6 to your preferred default model<br/>



(optional)<br/>
run `python3 app.py &` or `python app.py &` to run the bot in background (linux)<br/>
add `python3 app.py &` or `python app.py &` to your startup apps for easy access after boot<br/>
change the `uModel` variable in line 10 to your preferred default model<br/>



