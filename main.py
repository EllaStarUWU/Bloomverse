from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.environ.get('TOKEN')

def start(update, context):
    update.message.reply_text("السَلَامُ عَلَيْكُم يا عسل🫠🎀\nو انا اقول ليه البوت نور🤏🍓✨")

def echo(update, context):
    text = update.message.text.strip()
    if text in ["السلام عليكم", "السلام عليكم ورحمة الله تعالىٰ وبركاته",
                "السلام عليكم ورحمة الله", "السَلَامُ عَلَيْكُم وَرَحْمَةُ اللّٰهِ تَعَالَىٰ وَبَرَكَاتُه"]:
        update.message.reply_text("وَعَلَيْكُم السَلَامُ وَرَحْمَةُ اللّٰهِ تَعَالَىٰ وَبَرَكَاتُه🌸🎀")
    if text in ["ق", "القوانين", "/القوانين"]:
        update.message.reply_text(
            "⋆｡° ✩ 🌸قوانين Bloomverse🌸 ✩ °｡⋆\n\n"
            "1. الاحترام أولاً:\n• تجنبي الكلمات الجارحة أو أي نقاشات حادة.\n"
            "• عاملِي الكل بلطف كما تحبين أن يُعاملوكِ (احتَرِم تُحتَرَم).\n\n"
            "2. المواضيع المسموحة:\n• النقاشات عن الألعاب، التصميمات، الإبداعات، والدردشة الودية.\n"
            "• يمنع الخروج عن موضوع الجروب بشكل يزعج الآخرين.\n\n"
            "3. ممنوع السبام:\n• لا ترسلي روابط عشوائية أو رسائل متكررة بدون سبب.\n\n"
            "4. المحتوى الآمن:\n• يُمنع إرسال أي محتوى غير لائق أو مخالف للدين.\n\n"
            "5. تفاعل بلطف:\n• شجعي البنات على مشاركة إبداعاتهن، ولا تنتقدي بشكل سلبي.\n\n"
            "6. إبلاغ الإدارة:\n• إذا كان في مشكلة أو مضايقة، أبلغي المشرفات أو الإدارة عند الضرورة.\n\n"
            "تذكري أن Bloomverse عالمنا الخاص، فخلينا نحافظ عليه🎀!"
        )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
