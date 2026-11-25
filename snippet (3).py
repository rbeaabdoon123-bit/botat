import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "9110494205:AAHswEBhqjTQX6337fPvxX-SLKKl3tSIx8Y"
BASE_URL = "https://www.xnxx.com/search/"

def search_xnxx(query: str):
    url = f"{BASE_URL}/{query}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        # ملاحظة: هذا الكود يفترض وجود هيكل HTML بسيط، في الواقع يتطلب استخدام مكتبة مثل BeautifulSoup لتحليل الصفحة وحساب الروابط بدقة
        # هنا نعيد رابط البحث مباشرة كنموذج بسيط كما طلبت
        return f"🔍 نتائج البحث لكلمة '{query}':\n{response.url}"
    except Exception: e:
        return f"حدث خطأ: {str(e)}"

async def handle_keyword(update: Update, context):
    text = update.message.text.strip()
    if text:
        result = search_xnxx(text)
        await update.message.reply_text(result)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keyword))
    application.run_polling()

if __name__ == "__main__":
    main()
