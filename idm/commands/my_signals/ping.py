from ...objects import dp, MySignalEvent
from ...utils import edit_message, new_message, delete_message, sticker_message
from datetime import datetime, date
import socket, time
import vkapi

@dp.my_signal_event_handle('пинг', 'пиу', 'кинг', 'п', 'пингб', 'тик', 'дон')
def ping(event: MySignalEvent) -> str:

    if event.command == 'пингб':
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message='PONG')
        return "ok"
    c_time = datetime.now().timestamp()
    delta = round(c_time - event.msg['date'], 3)

    #c_time_str = str(datetime.fromtimestamp(round(c_time)))
    #v_time_str = str(datetime.fromtimestamp(round(event.msg['date'])))

    r_type = ('ПОНГ' if event.command == "пинг" else "ПАУ"
    if event.command == "пиу" else "ЧИКИ БОН" if event.command == "дон" else "ТАК" if event.command == "тик" else "КОНГ"  )
    if delta > 15:r_type += "\nЯ ЕБАЛ ТОМУ ЕБАЛО, ЯРИК БОЧЕК ПОТИК, ВРЕМЯ БЛЯТЬ БОЛЬШЕ 15 СЕК, БЕДЫ С VK_API"
    elif delta > 10:r_type += "\nЯ ЕБАЛ ТОМУ ЕБАЛО, ЯРИК БОЧЕК ПРОТИКАЕТ, ВРЕМЯ ОТВЕТА БОЛЬШЕ 10 СЕК"
    elif delta > 5:r_type += "\nЯРИК ВАДИЛА ВЫСШИЙ ПИЛОТАЖ, ВРЕМЯ ОТВЕТА БОЛЬШЕ 5 СЕК, НУ ЭТО НОРМ"
    else:r_type += "\nВАДИЛАМ ПРИВЕТ, ВРЕМЯ ОТВЕТА МЕНЬШЕ 5 СЕК, ЭТО КЛАСС"
    message = f"""{r_type} N2G

    Время ответа: {delta} с.
    """.replace('    ', '')

    if event.db.adv[0] == 'CB-LP':
        items = event.api('messages.getHistory', peer_id = event.chat.peer_id,
        count = 20)['items']
        for item in items:
            if item['out'] == 1 and 'LP\nОтвет за' in item['text']:
                edit_message(event.api, event.chat.peer_id, item['id'],
                message = item['text'] + '\n\n' + message)
                delete_message(event.api, event.chat.peer_id, event.msg['id'])
                message = 0
                break
        if message != 0:
            edit_message(event.api, event.chat.peer_id, event.msg['id'],
            message = f'{message}\n\nОтвет LP не нашел :/')
    else:
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=message)
    return "ok"


