import asyncio
from random import choice, randint

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from . import ALIVE_NAME, catub, edit_delete, edit_or_reply, get_user_from_event

plugin_category = "fun"


@catub.cat_cmd(
    pattern="وهمي(?: |$)(.*)",
    command=("وهمي", plugin_category),
    info={
        "header": "To show fake actions for a paticular period of time",
        "description": "if time is not mentioned then it may choose random time 5 or 6 mintues for mentioning time use in seconds",
        "usage": [
            "{tr}scam <action> <time(in seconds)>",
            "{tr}scam <action>",
            "{tr}scam",
        ],
        "examples": "{tr}scam photo 300",
        "actions": [
            "كتابة",
            "جهة",
            "لعبة",
            "موقع",
            "صوتية",
            "جولة",
            "فيديو",
            "صورة",
            "ملف",
        ],
    },
)
async def _(event):
    options = [
        "كتابة",
            "جهة",
            "لعبة",
            "موقع",
            "صوتية",
            "جولة",
            "فيديو",
            "صورة",
            "ملف",
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:
        scam_action = choice(options)
        scam_time = randint(300, 360)
    elif len(args) == 1:
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(300, 360)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await edit_delete(event, "`خطأ كتابة الجملة !!`")
        return
    try:
        if scam_time > 0:
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await asyncio.sleep(scam_time)
    except BaseException:
        return


@catub.cat_cmd(
    pattern="ارفعه(?: |$)(.*)",
    command=("ارفعه", plugin_category),
    info={
        "header": "To promote a person without admin rights",
        "note": "You need proper rights for this",
        "usage": [
            "{tr}prankpromote <userid/username/reply>",
            "{tr}prankpromote <userid/username/reply> <custom title>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To promote a person without admin rights"
    new_rights = ChatAdminRights(post_messages=True)
    catevent = await edit_or_reply(event, "**جـاري رفع مشرف....**")
    user, rank = await get_user_from_event(event, catevent)
    if not rank:
        rank = "Admin"
    if not user:
        return
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    await catevent.edit("**تم رفعه بنجاح خلص ذا كانت مزحه امر تسلية 😹🙁**")


@catub.cat_cmd(
    pattern="مشرف$",
    command=("مشرف", plugin_category),
    info={
        "header": "Fun animation for faking user promotion",
        "description": "An animation that shows enabling all permissions to him that he is admin(fake promotion)",
        "usage": "{tr}padmin",
    },
    groups_only=True,
)
async def _(event):
    "Fun animation for faking user promotion."
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "**جـاري رفع مشرف.......**")
    animation_chars = [
        "**جـاري رفع مشرف...**",
        "**تمكين كافة أذونات المستخدم ...**",
        "**(1) إرسل رسائل: ☑️**",
        "**(1) إرسل رسائل: ✅**",
        "**(2) إرسال الوسائط: ☑️**",
        "**(2) إرسال الوسائط: ✅**",
        "**(3) إرسال ملصقات وصور GIF: ☑️**",
        "**(3) إرسال ملصقات وصور GIF: ✅**",
        "**(4) إرسال استطلاعات الرأي: ☑️**",
        "**(4) إرسال استطلاعات الرأي: ✅**",
        "**(5) روابط التضمين: ☑️**",
        "**(5) روابط التضمين: ✅**",
        "**(6) أضف مستخدمين: ☑️**",
        "**(6) أضف مستخدمين: ✅**",
        "**(7) تثبيت الرسائل: ☑️**",
        "**(7) تثبيت الرسائل: ✅**",
        "**(8) تغيير معلومات الدردشة: ☑️**",
        "**(8) تغيير معلومات الدردشة: ✅**",
        "**تم منح الإذن بنجاح**",
        f"**امتيازات عامة : {DEFAULTUSER}**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])
