@iqthon.iq_cmd(
    pattern="اطفاء تليثون$",
    command=("اطفاء تليثون", plugin_category),
    info={
        "header": "♰︙ إيقاف التشغيـل ✕",
        "description": "♰︙لإيقـاف الدايـنو لموقـع هيروڪو، عندها لايمڪنك التشغيـل من البوت وبذلك عليك الذهـاب لموقـع هيروڪو لتشغيـله 💡",
        "usage": "{tr}اطفاء تليثون",
    },
)
async def _(event):
    "♰︙ إيقاف التشغيـل ✕"
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**⌔︙ إيقاف التشغيـل ✕ **\n" "**⌔︙ تـم إيقـاف تشغيـل البـوت بنجـاح ✓**",
        )
    await edit_or_reply(
        event,
        "**♰︙جـاري إيقـاف تشغيـل البـوت الآن ..**\n **أعـد تشغيـلي يدويـاً لاحقـاً عـبر هيـروڪو ..**\n**سيبقى البـوت متوقفـاً عن العمـل لغايـة** \n**الوقـت المذڪـور 💡**",
    )
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)
