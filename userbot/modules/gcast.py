from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Pesannya Mana Cokk???`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Sabar Ya Cokk, Gcast Mulu kena limit mampus Whahaha...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")
    await kk.reply("`Mudahan Kena LIMIT Akwoakwoa`")


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Pesan nya Mana Cokk???`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan ke Obrolan2 (Bukan Grup)...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")
    await kk.reply("`Mudahan Di Report Biar Kena Limit WKWKWKWK`")


CMD_HELP.update(
    {
        "gcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gcast`\
         \n↳ : Mengirim Pesan Group Secara Global."})

CMD_HELP.update(
    {
         "gucast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global ke Obrolan (Bukan Grup)."
    }
)
