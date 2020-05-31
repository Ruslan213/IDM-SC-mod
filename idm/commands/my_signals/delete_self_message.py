from ...objects import dp, MySignalEvent
from ... import utils
from datetime import datetime
from vkapi import VkApiResponseException
import time

@dp.my_signal_event_handle('-смс', 'dsm', '-смсб', 'дд')
def delete_self_message(event: MySignalEvent) -> str:
    message_id = event.msg['id']
    utils.edit_message(event.api, event.chat.peer_id, message_id, message="не буду удалять, сам удаляй")
    time.sleep(3)
    utils.edit_message(event.api, event.chat.peer_id, message_id, message="я скакзал НЕ БУДУ")
    user_id = event.msg['from_id']
    if event.command == '-смсб':
        period = 1800
    else:
        period = 86400

    try:
        #amount = " ".join(event.args)
        amount = int(event.args[0]) + 1
    except:
        amount = 2

    msg_ids = []
    for mmsg in utils.get_all_history_gen(event.api, event.chat.peer_id):
        if datetime.now().timestamp() - mmsg['date'] > period:
            break
        if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
            msg_ids.append(str(mmsg['id']))

    if amount != None:
        if amount <= len(msg_ids):
            msg_ids = msg_ids[:len(msg_ids) - (len(msg_ids) - amount)]

    message_id = 0
    try:
        event.api("messages.delete", message_ids=",".join(msg_ids), delete_for_all=1)
        message_id = utils.new_message(event.api, event.chat.peer_id, message="✅ ГОТОВО НАХУЙ, ВСЁ БЛЯТЬ, У МЕНЯ ПЕРЕРЫВ")
    except VkApiResponseException as e:
        if e.error_code == 924:
            message_id = utils.new_message(event.api, event.chat.peer_id, message="❗ Не удалось удалить сообщения.")
        else:
            message_id = utils.new_message(event.api, event.chat.peer_id, message=f"❗ Не удалось удалить сообщения. Ошибка VK {e.error_msg}")
    except:
        message_id = utils.new_message(event.api, event.chat.peer_id, message=f"❗ Произошла неизвестная ошибка.")

    time.sleep(2)
    utils.delete_message(event.api, event.chat.peer_id, message_id)
    return "ok"
