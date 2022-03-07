""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Channel Support :** [Mikoo Userbot](t.me/MikooUserbot)\n"
        f"✣ **Owner Repo :** [DivaArvian](t.me/divarvian)\n"
        f"✣ **Repo :** [Mikoo-Userbot](https://github.com/divarvian/Mikoo-Userbot)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Mikoo-Userbot:** [KLIK DISINI](https://github.com/divarvian/Mikoo-Userbot)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Mikoo-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Mikoo-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Mikoo-Userbot.\
    "
    }
)
