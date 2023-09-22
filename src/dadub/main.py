import discord
import aiohttp
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

TOKEN = "your_bot_token" # Enter Token (as string)

TARGET_CHANNEL_ID = 0000000000000000000 # Enter Discord Channel (as int)


# Define the file type extensions (ext) you want to download
FILE_TYPES = ['.jpg', '.png', '.gif', '.pdf'] # Default to images and pdf, but works with any file extension (wav, mp3, mov, etc)

DOWNLOAD_DIR = 'downloaded_files'

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user.name}')
    
    # Fetch all messages in the target channel
    target_channel = client.get_channel(TARGET_CHANNEL_ID)
    if target_channel:
        async for message in target_channel.history(limit=None):  # None to fetch all messages
            if message.attachments:
                for attachment in message.attachments:
                    if any(attachment.filename.endswith(ext) for ext in FILE_TYPES): # Get all files matching selected exrensions
                        async with aiohttp.ClientSession() as session:
                            async with session.get(attachment.url) as resp:
                                if resp.status == 200:
                                    filename = os.path.join(DOWNLOAD_DIR, attachment.filename)
                                    with open(filename, 'wb') as f:
                                        f.write(await resp.read())
                                    print(f'Downloaded: {filename}')
                                    downloaded_files = True

    if downloaded_files:
        print("Done")
        await client.close()
    else:
        print("No matching files found.")
        await client.close()


if __name__ == "__main__":
    if TOKEN == "your_bot_token" or TARGET_CHANNEL_ID == 0000000000000000000:
        print("Error: You have to change token and channel.")
    else:
        client.run(TOKEN)
