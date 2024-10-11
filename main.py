import telebot
import datetime
import time
import threading

bot = telebot.TeleBot('введите ваш токен')
# Путь к файлу с текстом объявления
announcement_text_path = "/Users/hametovviktor/PycharmProjects/pythonProject/announcement.txt"
announcement_photo_path = "/Users/hametovviktor/Downloads/2024-10-03 16.39.06.jpg"  # Путь к изображению
# Чтение текста объявления из файла
with open(announcement_text_path, 'r') as file:
    text = file.read()
# Список chat_id, куда будет отправляться сообщение 231399891, 231399891, 4162040231, 4162040231 глеб
chat_ids = "list_chat_id"  # Добавьте сюда другие chat_id
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Здравствуйте! Я чат бот, который поможет приобрести оборудование или товары от КофеЛавки")
def send_announcement():
    while True:
        now = datetime.datetime.now()
        # Отправка объявления по понедельникам и четвергам в 17:40
        if (now.weekday() == 0 or now.weekday() == 4) and now.hour == 15 and now.minute == 16:
            # Отправляем текст и фото всем из списка chat_ids
            with open(announcement_photo_path, 'rb') as photo:
                for chat_id in chat_ids:
                    try:
                        bot.send_photo(chat_id=chat_id, photo=photo, caption=text)
                    except Exception as e:
                        print(f"Не удалось отправить сообщение пользователю с chat_id {chat_id}: {e}")
            time.sleep(60)  # Ждем минуту, чтобы избежать повторной отправки в течение одной минуты
        time.sleep(30)  # Проверяем каждые 30 секунд

# Запускаем поток для отправки объявлений
threading.Thread(target=send_announcement, daemon=True).start()

bot.polling(non_stop=True)