from bot import create_app

app = create_app()

print("🔥 BETBOT PRO RUNNING...")

app.run_polling()
