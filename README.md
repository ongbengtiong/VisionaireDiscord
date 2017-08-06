# VisionaireDiscord
Discord
Create a new app in Discord: https://discordapp.com/developers/applications/me
Grab the client ID and Token.

https://discordapp.com/oauth2/authorize?client_id=<client_id>&scope=bot&permissions=0


Heroku
Install Heroku CLI
> heroku login
> heroku create --buildpack https://github.com/heroku/heroku-buildpack-python.git

Use python to create "src/com/squeakysnail/visionairediscord/bot.py" file for running the bot.
Use PyDev with Eclipse
required libraries: pip install discord.py, etc. See requirements.txt

> heroku local #to try running locally
> pip freeze > requirements.txt
# create app.json
> echo "worker: python src/com/squeakysnail/visionairediscord/bot.py" > Procfile
> git push heroku master 


In Heroku web console, make "worker python src/com/squeakysnail/visionairediscord/bot.py" is turned on.


