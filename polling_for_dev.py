import django

django.setup()

from bot_logic.views import *

if __name__ == '__main__':
    print('start')
    while True:
        try:
            bot.polling(none_stop=True)
        except ConnectionError as e:
            print(e)
            continue
