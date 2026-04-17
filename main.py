from bot import create_app

app = create_app()

print("🔥 Bot running...")

app.run_polling()
