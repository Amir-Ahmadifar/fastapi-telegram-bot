<div align="center">
  <img src="https://github.com/Amir-Ahmadifar/fastapi-telegram-bot/issues/1#issue-3455235835" alt="FastAPI Telegram Bot" />
  <br><br>

  <p align="center">
    <a href="https://instagram.com/" rel="nofollow" target="_blank">
      <img src="https://img.shields.io/badge/Instagram-@ami.r_ahmadii-E4405F?logo=instagram&style=for-the-badge" alt="Follow on Instagram" />
    </a>
    <a href="https://t.me/amirahmadifaar" rel="nofollow" target="_blank">
      <img src="https://img.shields.io/badge/Telegram-@amirahmadifaar-26A5E4?logo=telegram&style=for-the-badge" alt="Chat on Telegram" />
    </a>
    <br><br>
    <a href="https://www.linkedin.com/in/amir-mohammad-ahmadifar-8a576b266" rel="nofollow" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-amir-0077B5?logo=linkedin&style=for-the-badge" alt="Connect on LinkedIn" />
    </a>
    <a href="https://am-ahmadifar.ir" rel="nofollow" target="_blank">
      <img src="https://img.shields.io/badge/Website-AmirMohammadAhmadifar-4A90E2?logo=world&style=for-the-badge" alt="Visit my Website" />
    </a>
  </p>
</div>

# FastAPI Telegram Bot

This is a **Telegram bot** built with [FastAPI](https://fastapi.tiangolo.com/) that works securely using **webhooks** and can be easily deployed with **Docker**.  
It can serve as a great template for developers who want to combine **Telegram Bots** with modern **REST APIs**.

---

# 🚀 Features
- ⚡ Powered by **FastAPI**
- 🔒 Secure communication via **webhooks**
- 🐳 Docker-ready for easy deployment
- 📦 Clean project structure to use as a **starter template**
- 🤖 Simple integration between Telegram Bot API and FastAPI

---

# 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/Amir-Ahmadifar/fastapi-telegram-bot.git
cd fastapi-telegram-bot
```

2. Create & activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux & Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environment variables
Create a .env file in the project root:

```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
WEBHOOK_URL=https://your-domain.com/webhook
```

5. Run locally

```bash
uvicorn app.main:app --reload
```

# 🐳 Run with Docker

1. Build Docker image:

```bash
docker build -t fastapi-telegram-bot .
```

2. Run container:

```bash
docker run -d -p 8000:8000 --name telegram-bot fastapi-telegram-bot
```

# 📡 Setup Telegram Webhook

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=<YOUR_DOMAIN>/webhook"
```
Replace <YOUR_BOT_TOKEN> with your bot token and <YOUR_DOMAIN> with your server domain.

Check if webhook is set correctly:

```bash
curl -X GET "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo"
```

# 🌍 Website

Check out my personal blog: https://am-ahmadifar.ir
I’d be happy to receive any feedback or suggestions!

# 📜 License

This project is open-sourced software licensed under the Apache 2.0 license.