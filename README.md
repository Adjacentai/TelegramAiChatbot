# AI-Powered Telegram Bot

## Description

This project is a Telegram bot integrated with a local AI model launched on **Olama**. The bot accepts user messages, processes them using AI, and returns intelligent responses. It supports dialog context management and includes a reset feature through a button.

## Features
1. Message processing and analysis via AI.
2. Dialog context management.
3. Integration with a local AI model running on **Olama**.
4. Reset button for clearing dialog context.
5. Message length validation.

## Installation

1. Clone the repository and install dependencies:

```
git clone <URL>
cd <project-directory>
pip install -r requirements.txt
```
   
2. Set up a .env file with your API keys and the AI server URL:
   
```
TG_API=<Your Telegram bot token>
OPENAI_API=<Your OpenAI API key>
MODEL_URL=<URL of your local AI server>
MODEL_NAME=<Name of the model on your server>
```
Launch the local AI server using Olama.

Run the bot:

```
python main.py
```
Main Files

aibot.py: Handles interaction with the local AI model.
bot.py: Sets up and runs the Telegram bot.
commands.py: Processes commands and user messages.
