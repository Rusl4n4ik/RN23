from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")


# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while (perc < 100):
        try:
            text = "👮 Hacking your ass ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Ass hacked successfully!")
    sleep(3)

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def heart(_, msg):
    perc = 0

    while (perc < 100):
        try:
            text = "Hacking your heart 💗 ... " + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("✅ Heart successfully hacked! 💖")
    sleep(3)

    # msg.edit("👽 Поиск секретных данных об НЛО ...")
    # perc = 0
    #
    # while (perc < 100):
    #     try:
    #         text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
    #         msg.edit(text)
    #
    #         perc += random.randint(1, 5)
    #         sleep(0.15)
    #
    #     except FloodWait as e:
    #         sleep(e.x)
    #
    # msg.edit("🦖 Найдены данные о существовании динозавров на земле!")


@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]

    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]

    random.shuffle(members)

    app.send_message(chat, "Щелчок Таноса ... *щёлк*")

    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)

    app.send_message(chat, "Но какой ценой?")


@app.on_message(filters.command('dem', prefixes='.') & filters.me)
def demotivation(_, msg):
    msg.edit('**Демотивируем...**')
    ms_id = msg["message_id"]
    id = msg['chat']['id']
    mess_id = msg['reply_to_message']['message_id']
    app.forward_messages(from_chat_id=id, chat_id="@super_rjaka_demotivator_bot", message_ids=mess_id,)
    sleep(2)
    demovat = app.get_history('@super_rjaka_demotivator_bot', limit=1)
    demovat2 = app.get_history('@super_rjaka_demotivator_bot', limit=1)
    while demovat == demovat2:
        demovat2 = app.get_history('@super_rjaka_demotivator_bot', limit=1)
        sleep(1)
    demovat2 = app.get_history('@super_rjaka_demotivator_bot', limit=1)
    fimaly = demovat2[0]["message_id"]
    app.forward_messages(from_chat_id='@super_rjaka_demotivator_bot', chat_id=id, message_ids=fimaly,)
    app.delete_messages(id, ms_id)

@app.on_message(filters.command('auf', prefixes='.')& filters.me)
def volk(_, msg):
    msg.edit('.◢🐺◣            ◢🐺◣\n'
             '🐺🐺🐺◣ ◢🐺🐺🐺\n'
             '◥🐺🐺🐺🐺🐺🐺◤\n'
             '    ◥🐺🐺🐺🐺◤\n'
             '         ◥☝️☝️◤\n'
             '             ◥ ◤')


@app.on_message(filters.command('moon', prefixes='.')& filters.me)
def moon(_,msg):
    moon_cycle = ['⠀🌑⠀', '⠀🌒⠀', '⠀🌓⠀', '⠀🌖⠀', '⠀🌕⠀', '⠀🌖⠀', '⠀🌗⠀','⠀🌘⠀','⠀🌑⠀']
    for i in moon_cycle:
        print(i)
        time.sleep(0.1)
        msg.edit(i)


@app.on_message(filters.command('hearts', prefixes='.')& filters.me)
def hearts(_,msg):
    moon_cycle = ['⠀❤⠀','⠀🧡⠀','⠀💛⠀','⠀💚⠀','⠀💙⠀','⠀💜⠀','⠀🖤⠀','⠀🤍⠀','⠀🤎⠀','⠀💔⠀','⠀❤⠀']
    for i in moon_cycle:
        print(i)
        time.sleep(0.2)
        msg.edit(i)


REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}


@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)



app.run()