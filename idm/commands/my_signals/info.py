from ...objects import dp, MySignalEvent, SignalEvent
from ...utils import edit_message, new_message
from datetime import datetime
from idm import __version__
import typing

@dp.my_signal_event_handle('инфо', 'инфа', '-i', 'info')
def info(event: typing.Union[MySignalEvent, SignalEvent]) -> str:

    owner = event.api('users.get', user_ids=event.db.owner_id)[0]


    message = f"""Информация о дежурном:
данная дежурка сделана на основе дежурного ириса, только с личными доп. командами
    Владелец: [id{owner['id']}|{owner['first_name']} {owner['last_name']}]
    Чатов: {len(event.db.chats.keys())}
    Создатель данного скрипта @id94282266 (Котя)
    программа выполнена на языке Python 3.8
    Информация о чате:
    Я {'' if event.chat.installed else 'не'} дежурный в чате {'✅' if event.chat.installed else '❌'}
    Iris ID: {event.chat.iris_id}
    Имя: {event.chat.name}

    """.replace('    ', '')

    edit_message(event.api, event.chat.peer_id, event.msg['id'],
    message=message, disable_mentions = 1)
    return "ok"
