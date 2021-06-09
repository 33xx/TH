# Userbot module for fetching info about any user on Telegram(including you!).

import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from userbot import catub
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch

plugin_category = "utils"
LOGS = logging.getLogger(__name__)


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "هذا المستخدم لم يضع اي صوره"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "Couldn't fetch DC ID!"
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس لديه اسم اول")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("لايوجد معرف")
    user_bio = "لاتوجد نبذه" if not user_bio else user_bio
    caption = "<b><i> 𓆩JMTHON SOURCE 𓆪 </i></b>\n"
    caption += f"<b> ⌁ | الأسم :</b> {first_name} {last_name}\n"
    caption += f"<b> ⌁ | الـمعرف :</b> {username}\n"
    caption += f"<b> ⌁ | الايدي :</b> <code>{user_id}</code>\n"
    caption += f"<b> ⌁ | عـدد الصور :</b> {replied_user_profile_photos_count}\n"
    caption += f"<b> ⌁ | النبـذة : </b> {user_bio} \n"
    caption += f"<b> ⌁ | حـسابه :</b> href=tg://user?id={user_id}>{first_name} \n\n"
    caption += f"<b> ⌁ | الـمطور </b>  [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)"
    return photo, caption


@catub.cat_cmd(
    pattern="كشف(?: |$)(.*)",
    command=("كشف", plugin_category),
    info={
        "الامر": "امر الكشف يقوم بإرسال بعض معلومات الشهص مم المجموعات المشتركه والخ  ، ",
        "الشرح": "للحصول على بعض معلومات الشخص.",
        "الاستخدام": "{tr}كشف <المعرف/ايدي/بالرد عليه>",
    },
)
async def _(event):
    "Gets information of an user such as restrictions ban by spamwatch or cas"
    replied_user, error_i_a = await get_user_from_event(event)
    if not replied_user:
        return
    catevent = await edit_or_reply(event, "**يتم حساب المعلومات**")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_id = replied_user.user.id
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their
        # names
        first_name = first_name.replace("\u2060", "")
    # inspired by https://telegram.dog/afsaI181
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "Couldn't fetch DC ID!"
    if spamwatch:
        ban = spamwatch.get_ban(user_id)
        if ban:
            sw = f"**Spamwatch Banned :** `True` \n       **-**🤷‍♂️**Reason : **`{ban.reason}`"
        else:
            sw = f"**Spamwatch Banned :** `False`"
    else:
        sw = "**Spamwatch Banned :**`Not Connected`"
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    if data:
        if data["ok"]:
            cas = "**Antispam(CAS) Banned :** `True`"
        else:
            cas = "**Antispam(CAS) Banned :** `False`"
    else:
        cas = "**Antispam(CAS) Banned :** `Couldn't Fetch`"
    caption = """**معلومات [{}](tg://user?id={}):
   -🔖 الايدي : **`{}`
   **-**👥**المجموعات المشتركة : **`{}`
   **-**🌏**رقم قاعدة البيانات : **`{}`
   **-**🔏**حسـاب موثق : **`{}`
   **-**🦅{}
   **-**👮‍♂️{}
""".format(
        first_name,
        user_id,
        user_id,
        common_chats,
        dc_id,
        replied_user.user.restricted,
        sw,
        cas,
    )
    await edit_or_reply(catevent, caption)


@catub.cat_cmd(
    pattern="ايدي(?: |$)(.*)",
    command=("ايدي", plugin_category),
    info={
        "الامر": "Gets info of an user.",
        "الشرح": "User compelete details.",
        "الاستخدام": "{tr}whois <username/userid/reply>",
    },
)
async def who(event):
    "Gets info of an user"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user, reason = await get_user_from_event(event)
    if not replied_user:
        return
    cat = await edit_or_reply(event, "**يتم الحصول على المعلومات**")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "** لا يمكن الحصول على معلومات هذا المستخدم**")
    message_id_to_reply = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")


@catub.cat_cmd(
    pattern="رابط الحساب?: |$)(.*)",
    command=("رابط الحساب", plugin_category),
    info={
        "الامر": "يقوم بصنع رابط لحساب اي شخص حتى لو غير معرفه سيبقى الرابط شغال .",
        "الاستخدام": "{tr}رابط الحساب <معرف/ايدي/بالرد عليه>",
    },
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id})")
