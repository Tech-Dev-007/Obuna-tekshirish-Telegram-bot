# Botni ishlatishdan oldin botni kanalizga Admin qiling bo'lmasa ishlamaydi
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

#Telegram bot tokenini o'zgartiring
TOKEN = 'BOT_TOKEN'

bot = telegram.Bot(token=TOKEN)

def start_handler(update, context):
    # InlineKeyboardMarkup obyektini yaratish
    check_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Obuna Bo'lish", url='https://t.me/username'),
                InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs")
            ]
        ]
    )
    # Start habarini yuborish
    update.message.reply_text("Assalomu alaykum! Botimizga xush kelibsiz.", reply_markup=check_button)

def button_handler(update, context):
    query = update.callback_query
    # Obunani tekshirish tugmasi bosilganda
    if query.data == 'check_subs':
        print("Ishlayabdi")
        chat_id = query.message.chat_id
        try:
            # Bot kanaliga obuna bo'lib bo'lmaganligini tekshirish
            print(f'Checking subscription status for chat ID {chat_id}')
            chat_member = bot.get_chat_member(chat_id='@username', user_id=chat_id)
            if chat_member.status in ['member', 'creator', 'administrator']:
                print("User is member")
                query.answer(text='✅ Siz kanalga obuna bo\'lgansiz!')
            else:
                query.answer(text='❌ Siz hali kanalga obuna bo\'lmagansiz!')
        except Exception as e:
            print(f'Exception occurred: {str(e)}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_handler))
    dp.add_handler(CallbackQueryHandler(button_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()