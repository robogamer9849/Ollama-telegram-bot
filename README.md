# Ollama-telegram-bot
a telegram bot for ollama

commads:<br/>
`/list_models`: list available models<br/>
`/"modelName"`: change the model<br/>
`/moedel`: tell what model you are using<br/>
`/help`: list commands<br/>

a log file named **OllamaBotLogs.log** will be created next to the **FILENAME.py** to show logs to the bot owner. it shows:<br/>
_when someone started the bot_<br/>
_what model did someone ask from_<br/>
_what command did someone use_<br/>

it doesn't show:<br/>
_who did those things_<br/>

!!you must have [ollama](https://ollama.com) installed for this to work!!<br/>

installation:<br/>
1.install [python](https://python.org)

2.install requirements:  (go to their github page if you cant use **pip**)<br/>
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI): `pip install pyTelegramBotAPI`<br/>
[Ollama Python Library](https://github.com/ollama/ollama-python): `pip install ollama`

3.download the latest version from releses part of this page and extract it(the one from the files is the oldest version)<br/>
3.5:<br/>
bot.multiple.log: makes a file named OllamaBotLogs{date}.log every time you run the app and keeps the old logs<br/>
bot.single.log: makes a single OllamaBotLogs.log and overwrites it every time the bot is ran


4.make a bot in [botfother](https://t.me/BotFather) (start by typing **/newbot** and the do what it tells you)<br/>

5.extract downloaded file

6.replace `token` value in config.py with the token that you got from botfather<br/>

7.open terminal and cd to the folder you put the downloaded _.py_ file in: `cd PATH/TO/FILE.PY`<br/>

8.start the bot: run `python3 FILENAME.py` or `python FILENAME.py` in terminal<br/>


(optional)<br/>
run `python3 FILENAME &` or `python FILENAME.py &` to run the bot in background (linux)<br/>
add `python3 PATH/TO/FILE.PY` or `python PATH/TO/FILE.PY` to your startup apps for easy access after boot<br/>
change the `default_model` in config.py to your preferred default model<br/>
add models to `ex_models` list in config.py to remove them from the bot



