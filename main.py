from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
from config import *
import sys
import re
import os

bot = Client("bot",
             bot_token= "6886091369:AAEQxJhJNcgW9DHK6hW8nAOlLCTYsrpkbek",
             api_id= 21408627,
             api_hash= "465cca6fa782695983d49db306e0f8be"
)

@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"Hi 👋 Sir ! How are You?\n\n☞ I'm a High Speed **Txt File** Downloader Bot.\n\n☞ I can Download **Videos & Pdf** From Your **TXT** File.\n\n**𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 :** 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇\n")
  

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Process Has Been Stopped Successfully !**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["pip"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"**Now Send Me Your **txt** File & Follow Bot Instructions**")
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(-1002080881254, x)
        await input.delete(True)
        file_name, ext = os.path.splitext(os.path.basename(x))
        

        path = f"./downloads/{m.chat.id}"

        try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")
            links = []
            for i in content:
                links.append(i.split("://", 1))
            os.remove(x)
            # print(len(links)
        except:
            await m.reply_text("Invalid file input.🥲")
            os.remove(x)
            return
    else:
        content = input.text
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
   
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend Number From Where You want to Download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or Send `d` To Grab Batch Name From Txt File**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter Resolution Ex :** 480 or 720")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name**\n**Ex : ** hhh")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3

    await editable.edit("Now Send Your **Thumb url**\nEg : `https://telegra.ph/file/7b060bedc493fa9be744f.jpg`\n\nOr Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
              
            elif 'classplusapp' in url:
                  headers = {
                      'Host': 'api.classplusapp.com',
                      'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NTA5MTAzNjYsIm9yZ0lkIjo0MDU0NzMsInR5cGUiOjEsIm1vYmlsZSI6IjkxOTUyMDAzNjgzNCIsIm5hbWUiOiJSYW1wYWwiLCJlbWFpbCI6InNoYWxpbmlzaGFybWExNTA2OEBnbWFpbC5jb20iLCJpc0ludGVybmF0aW9uYWwiOjAsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImNvdW50cnlJU08iOiI5MSIsInRpbWV6b25lIjoiR01UKzU6MzAiLCJpc0RpeSI6ZmFsc2UsImZpbmdlcnByaW50SWQiOiI5MWU0MTYyODMxNjQxZGFjMTAzYWMyNGMzYjQxNTg4YyIsImlhdCI6MTY4MDI5NTY4MSwiZXhwIjoxNjgwOTAwNDgxfQ.q_iVpHJ1jgpHvb_v3b35AiyjrnW34PuWs00T5tWdyJn9Cm5tzI3ndKhY8I_sPmyn',
                      'user-agent': 'Mobile-Android',
                      'app-version': '1.4.37.1',
                      'api-version': '18',
                      'device-id': '5d0d17ac8b3c9f51',
                      'device-details':'2848b866799971ca_2848b8667a33216c_SDK-30',
                      'accept-encoding': 'gzip, deflate' }
                
                  params = (('url', f'{url}'), )
                  response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)                
                  url = response.json()['url']

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'[ 🎬 ] **Vid ID : **{str(count).zfill(3)}\n**Video Title :** {name1}({res}) 『 hhh』.mp4\n**Batch Name :** {b_name}\n\n**Extracted By ➤** {CR}'
                cc1 = f'[ 📕 ] **Pdf ID : **{str(count).zfill(3)}\n**File Title :** {name1} 『 hhh 』.pdf\n**Batch Name :**{b_name}\n\n**Extracted By ➤** {CR}'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        await copy.copy(chat_id = -1002080881254)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id,document=f'{name}.pdf', caption=cc1)
                        await copy.copy(chat_id = -1002080881254)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    prog = await m.reply_text(f"**Downloading:-**\n\n**Title ➤** `{name}`\n**Quality ➤** `{raw_text2}`\n\n**Bot By ➤ **hhh")
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name)
                    count += 1

            except Exception as e:
                await m.reply_text(f"**This #Failed File is not Counted**\n**Name ➤** `{name}`\n**Link ➤** `{url}`\n\n ** Failed Reason ➤** {e}")
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done ✅")
@bot.on_message(filters.command(["vpdf"]))
async def vision_pdf(bot: Client, m: Message):
    editable = await m.reply_text("Hi 👋 Sir!\n\nHow are You ?\n\n☞ I'm **Vision Pdf** Downloader Bot.\n\n☞ Send ' /vpdf ' Command to Download **Vision IAS** Pdf.\n\n☞ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇\n")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")

            links = []
            for i in content:
                links.append(i.split(":", 1))
            os.remove(x)
    except:
            await m.reply_text("Invalid file input.☹️")
            os.remove(x)
            return
            
    editable = await m.reply_text(f"Total links found are {len(links)}\n\nSend From Where You Want to Download,\n\nInitial is 1")
    input1: Message = await bot.listen(editable.chat.id)
    count = input1.text
    count = int(count)      	
    	            
    await m.reply_text("**Enter Your Batch Name**")
    inputy: Message = await bot.listen(editable.chat.id)
    raw_texty = inputy.text

    await m.reply_text("**Enter Cookie**")
    input2: Message = await bot.listen(editable.chat.id)
    cookie = input2.text
    cookies = cookies = {'PHPSESSID': f'{cookie}'}
        
    try:
        for i in range(count, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()[:57]
            name = f'{str(count).zfill(3)}) {name1}'
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n\n**Batch:-** {raw_texty}\n\n**Extracted By ➤** hhh '
            ka = await helper.vision(url, name, cookies)
            await m.reply_document(ka, caption=cc)
            count += 1
            os.remove(ka)
            time.sleep(3)
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done ✅")
    
bot.run()
