import os
from datetime import datetime

from userbot import jmthon

from . import reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/01f3b4b14a4a224e61f3a.mp4"
)

JM_TXT = os.environ.get("PING_TEXT") or "- New Style ⚙."


@jmthon.ar_cmd(
    pattern=".$",
    command=(".", plugin_category),
    info={
        "header": "امر تجربه البوت اذا يشتغل ارسل  .بنك متطور فقط",
        "option": "امر بنك المتطور كتابة  @DEOOUS",
        "usage": [
            "{tr}.",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(event, "<b><i>- MoH</b></i>", "html")
    end = datetime.now()
    await cat.delete()
    (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>t: @HmmHH"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )
