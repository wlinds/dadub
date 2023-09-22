# **dadub**
### Discord Attachment Downloader Utility Bot

Easily download any attatchment from any Discord Server.

Simple python script that allows you to download attachments (files) from a specified Discord channel. You can configure it to download specific file types, making it a useful tool for archiving media or documents shared in your Discord server.

## Dependencies

To run this script, you'll need the following dependencies:

- [discordpy](https://discordpy.readthedocs.io/en/latest/index.html#)

- [aiiohttp](https://docs.aiohttp.org)

## Installation

Clone this repository to your local machine:

```
git clone https://github.com/wlinds/dadub.git
```

Go to the project directory and ceate a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

On Windows:

```
venv\Scripts\activate
```

On macOS and Linux:

```
source venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

## Config


Before running the script, you need to configure a few settings in the main.py file:

Replace 'your_bot_token' with your actual Discord bot token.

Set TARGET_CHANNEL_ID to the ID of the Discord channel from which you want to download attachments.


Define the DOWNLOAD_DIR variable to specify the directory where downloaded files will be saved.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.