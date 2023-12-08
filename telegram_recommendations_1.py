from telethon import TelegramClient, types # pip install telethon
from telethon.tl import types, functions
import json

# Will not work if MFA is activated (password cloud)

# Use your own values from my.telegram.org

api_id =                    # number
api_hash = ''               # string
client = TelegramClient('anon', api_id, api_hash)

data = {}

async def main():

    async for dialog in client.iter_dialogs():

        if str(dialog.id).startswith("-100"):

            print(dialog.name, ";", dialog.id)

            try:
                my_channel = await client.get_entity(types.PeerChannel(dialog.id))
                recommendations = await client(functions.channels.GetChannelRecommendationsRequest(channel=my_channel))

                """
                if my_channel.username:
                    channel_link = "https://t.me/" + my_channel.username
                else:
                    channel_link = ""
                print(channel_link)
                """

                if len(recommendations.chats) > 0:

                    similar = {}
                    for chat in recommendations.chats:
                        subchannel_link = "https://t.me/" + chat.username
                        similar[chat.id] = {"chat_title": chat.title, "number_participants": chat.participants_count, "link": subchannel_link}
                    data[dialog.id] = {"chat_name": dialog.name, "similar_channels": similar}
                else:
                    print("No recommendations for this channel.")

                print(recommendations)
                print("\n")

            except Exception as e:
                print(e)
                pass

with client:
    client.loop.run_until_complete(main())

try:
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
except:
    print("Error with the json file.")
