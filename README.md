# ⚽ Bet-Football Bot

AI-powered football betting assistant bot built with Python.

## 🚀 Features

- Daily football matches (API-based)
- Statistical analysis (goals for / against)
- Match prediction system (xG model)
- Telegram bot integration
- Top 3 bets daily (morning & evening)

## 🧠 How it works

The bot uses real football data from API-Football:

- Fetches today's matches
- Gets team statistics
- Applies prediction model
- Sends best betting picks to Telegram

## 📂 Project Structure

- Bot.py → Telegram bot logic  
- api.py → Fetch matches & stats  
- predictor.py → Prediction engine  
- scheduler.py → Daily automation  
- main.py → Bot runner  
- config.py → API keys  

## ▶️ Run locally

```bash
pip install -r requirements.txt
python main.py
