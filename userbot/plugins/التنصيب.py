from userbot.utils import admin_cmd


@borg.on(admin_cmd("التنصيب"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "♰︙**مـرحبا بـك عزيـزي** \n♰︙رابط التنصيب - [اضغط هنا](http://2u.pw/btpnU)\n♰︙قناة السورس - @DEOOUS"
        )

@borg.on(admin_cmd("السورس"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "♰︙︎ ︎ ︎︎ ︎ ︎︎ ︎ ︎︎ ︎ ︎**سورس ديو الرسمي**\n\n ♰︙سورس ديو الرسمي - [اضغط هنا](http://t.me/deoous)\n♰︙قناة ديو الرسمية - @DEOOU\nأصـدار ديـو :♰ 4.0.0"
        )

