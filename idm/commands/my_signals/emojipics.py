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

@dp.my_signal_event_handle('ф', 'f')
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

@dp.my_signal_event_handle('луна')
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

@dp.my_signal_event_handle('ъуъ')
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





@dp.my_signal_event_handle('дурка')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'🕺      🚑',
'🕺     🚑',
'🕺    🚑',
'🕺   🚑',
'🕺  🚑',
'🕺 🚑',
'🕺🚑',
'🏥🏥🏥🏥🏥🏥🏥🏥\n🏥🚑Иди лечись🏥🏥\n🏥🏥🏥🏥🏥🏥🏥🏥',
]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(1)
    return "ok"



@dp.my_signal_event_handle('орешек')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n🚶\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
'И тут появляеться маньяк! \n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n🚶 🌳👹🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
'Он заметил маньяка \n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n😲 🙎‍♂🔪🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n',
'Парень хотел убежать но маньяк был быстрее\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳 \n🚶 👹🔪 🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
'Маньяк его убил!\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n😵 👹🔪 🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
'Но тут не далеко проезжала полиция и увидела убийство! \n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n👹🔪 !🚔!\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
'Маньяка посадили за решотку! \n||||||||||||| ||||||||||| |🚔🚔🚔 \n|| 👹 || || 👮 || |🚔🚔🚔 \n||||||||||||| ||||||||||| |🚔🚔🚔 ',
'Но они даже не предпологали что у маньяка есть бомба! \n||||||||||||| ||||||||||| |🚔🚔🚔 \n|| 👹 || || 👮 || |🚔🚔🚔 \n||||||||||||| ||||||||||| |🚔🚔🚔',
'||||||||||||| ||||||||||| |🚔🚔🚔\n||👹💣 || || 👮 || |🚔🚔🚔\n||||||||||||| ||||||||||| |🚔🚔🚔 ',
'ПИЗДОХС!!!! и нет участка \n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥 \n',
'Но ходят слухи что маньяк остался жив! \nХе-хе\nА ты проверял свой шкаф? 🤡👹🔪',

]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(2)
    return "ok"



@dp.my_signal_event_handle('секрет')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'а ты вкурсе что это секретная команда?',
'нет, не знал???',
'а че суешь свой нос куда тебя не просят?',
'за это я щас рекламу сделаю',
'хочешь такую же дежурку?\nпиши создателю данной дежурки @id94282266 (Котя)',
]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(2)
    return "ok"


@dp.my_signal_event_handle('школа')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'Ну чтож сегодня расскажу вам один секрет (как не пойти в школу) ',
'Хмммм',
'Начнем с того что вам нужно взять эти вещи: ',
'градусник, батарейка, вата, вода. ',
'Нужно взять крадусник ииии...',
'ИДИ НАХУЙ ШКОЛЬНИК ЕБАНЫЙ УЧИСЬ ДАВАЙ!',
]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(3)
    return "ok"




@dp.my_signal_event_handle('дежурный')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'Привет ',
'Я дежурный ириса ',
'Если хочешь быть таким же дежурным ',
'И если хочешь что бы все работало без лагов ',
'То тебе прийдеться дать доступ к аккаунту вк ',
'Если тебя все устраивает ',
'Пиши нашему создателю @id94282266 (Котя)',

]
    for i in range(len(pic)):
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message=f'{msg}\n\n{pic[i]}')
        time.sleep(3)
    return "ok"





@dp.my_signal_event_handle('дшабы')
def BFanim(event: MySignalEvent) -> str:
    msg = anim_reply(event.reply_message, event.api)
    pic = [
'вот все мои ДШабы:\n1. дурка\n2. орешек \n3 секрет\n4. школа',
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




