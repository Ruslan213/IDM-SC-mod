from ...objects import dp, MySignalEvent
from ...utils import edit_message, new_message
import time

def anim_reply(reply_msg, vk):
    if reply_msg:
        user = vk('users.get', user_ids=reply_msg['from_id'])[0]
        msg = f"[id{user['id']}|{user['first_name']} {user['last_name']}]"
    else:
        msg = ''
    return msg

@dp.my_signal_event_handle('')
def fpic(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    picl = ['🌕🌗🌑🌑🌑🌑🌑🌓🌕','🌕🌗🌑🌑🌑🌑🌑🌕🌕','🌕🌗🌑🌓🌕🌕🌕🌕🌕','🌕🌗🌑🌓🌕🌕🌕🌕🌕',
    '🌕🌗🌑🌑🌑🌑🌓🌕🌕','🌕🌗🌑🌑🌑🌑🌕🌕🌕','🌕🌗🌑🌓🌕🌕🌕🌕🌕','🌕🌗🌑🌓🌕🌕🌕🌕🌕','🌕🌗🌑🌓🌕🌕🌕🌕🌕']
    pic0 = picl[0]
    pic1 = picl[1]
    pic2 = picl[2]
    pic3 = picl[3]
    pic4 = picl[4]
    pic5 = picl[5]
    pic6 = picl[6]
    pic7 = picl[7]
    pic8 = picl[8]

    for i in range(10):
        edit_message(event.api, event.chat.peer_id, event.msg['id'],
        message=f'''{msg}\n\n{pic0}\n{pic1}\n{pic2}\n{pic3}\n{pic4}
            {pic5}\n{pic6}\n{pic7}\n{pic8}'''.replace('    ', ''))
        pic0 = pic0[-1:] + pic0[:-1]
        pic1 = pic1[-1:] + pic1[:-1]
        pic2 = pic2[-1:] + pic2[:-1]
        pic3 = pic3[-1:] + pic3[:-1]
        pic4 = pic4[-1:] + pic4[:-1]
        pic5 = pic5[-1:] + pic5[:-1]
        pic6 = pic6[-1:] + pic6[:-1]
        pic7 = pic7[-1:] + pic7[:-1]
        pic8 = pic8[-1:] + pic8[:-1]
        time.sleep(0.8)
    return "ok"

@dp.my_signal_event_handle('')
def notthisdezh(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    edit_message(event.api, event.chat.peer_id, event.msg['id'], message='⚠ Не в этом дежурном')
    time.sleep(3)
    edit_message(event.api, event.chat.peer_id, event.msg['id'], message='Ладно, хорошо, так уж и быть...')
    time.sleep(2)
    pic = '🌑🌒🌓🌔🌕🌖🌗🌘'
    for i in range(9):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic}')
        pic = pic[-1:] + pic[:-1]
        time.sleep(1)
    return "ok"

@dp.my_signal_event_handle('')
def jujpic(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    picl = [
'🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕','🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕','🌘🌑🌕🌕🌘🌑🌒🌕🌕🌕',
'🌑🌕🌕🌘🌑🌑🌑🌓🌕🌕','🌘🌔🌖🌑👁🌑👁🌓🌗🌒','🌖🌓🌗🌑🌑🌑🌑🌔🌕🌑',
'🌕🌗🌑🌑🌑🌑🌒🌕🌘🌒','🌕🌕🌘🌑🌑🌑🌑🌑🌒🌕','🌕🌕🌘🌑🌑🌑🌔🌕🌕🌕',
'🌕🌕🌘🌔🌘🌑🌕🌕🌕🌕','🌕🌖🌒🌕🌗🌒🌕🌕🌕🌕','🌕🌗🌓🌕🌗🌓🌕🌕🌕🌕']
    pic0 = picl[0]
    pic1 = picl[1]
    pic2 = picl[2]
    pic3 = picl[3]
    pic4 = picl[4]
    pic5 = picl[5]
    pic6 = picl[6]
    pic7 = picl[7]
    pic8 = picl[8]
    pic9 = picl[9]
    pic10 = picl[10]
    pic11 = picl[11]

    for i in range(11):
        edit_message(event.api, event.chat.peer_id, event.msg['id'],
message=f'''{msg}\n\n{pic0}\n{pic1}\n{pic2}\n{pic3}\n{pic4}\n{pic5}\n{pic6}
            {pic7}\n{pic8}\n{pic9}\n{pic10}\n{pic11}'''.replace('    ', ''))
        pic0 = pic0[-1:] + pic0[:-1]
        pic1 = pic1[-1:] + pic1[:-1]
        pic2 = pic2[-1:] + pic2[:-1]
        pic3 = pic3[-1:] + pic3[:-1]
        pic4 = pic4[-1:] + pic4[:-1]
        pic5 = pic5[-1:] + pic5[:-1]
        pic6 = pic6[-1:] + pic6[:-1]
        pic7 = pic7[-1:] + pic7[:-1]
        pic8 = pic8[-1:] + pic8[:-1]
        pic9 = pic9[-1:] + pic9[:-1]
        pic10 = pic10[-1:] + pic10[:-1]
        pic11 = pic11[-1:] + pic11[:-1]
        time.sleep(0.8)
    return "ok"



@dp.my_signal_event_handle('')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'',

]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(1)
    return "ok"


@dp.my_signal_event_handle('дшабы')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'вот все мои ДШабы:\n',
]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(1)
    return "ok"

@dp.my_signal_event_handle('удшабы')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'вот все мои ДШабы:',
]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(1)
    return "ok"






