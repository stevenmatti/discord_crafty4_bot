# discord_crafty4_bot
Creating discord bot to command crafty4 to start/stop minecraft server from discord

How someone else runs your project

1 Clone repo

git clone git@github.com:stevenmatti/discord_crafty4_bot.git
cd discord_crafty4_bot


2 Create their own virtual environment

python3 -m venv venv

3 Activate it

Linux/Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

4 Install dependencies

pip install -r requirements.txt

5 Create the .env file
Create a .env file in the project root:
touch .env

Add your Discord bot token:
DISCORD_TOKEN=your_discord_bot_token_here

Example:
DISCORD_TOKEN=MTExxxxxxxxxxxxxxxxxxxxxxxxxxxxx

⚠️ Never commit this file to Git (it should already be ignored in .gitignore).


6 Run your bot

python main.py
