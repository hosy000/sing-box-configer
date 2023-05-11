import json
import os
from telegram.ext import Updater, CommandHandler

# Define the json data to be modified
json_data = {
    "log": {
        "level": "info",
        "timestamp": True
    },
    "inbounds": [
        {
            "type": "vless",
            "tag": "vless-in",
            "listen": "::",
            "listen_port": 2222,
            "sniff": True,
            "sniff_override_destination": True,
            "domain_strategy": "ipv4_only",
            "users": [
                {
                    "uuid": "E66E8785-9284-493D-BF48-8232AA3686EA", 
                    "flow": "xtls-rprx-vision"
                }
            ],
            "tls": {
                "enabled": True,
                "server_name": "xxxxxxx",
                "reality": {
                    "enabled": True,
                    "handshake": {
                        "server": "xxxxxxx",
                        "server_port": 443
                    },
                    "private_key": "qAdSu-xtsEOlP-xfysiAdiU-NxUBWmxZ63OOnTEMFFk",
                    "short_id": [ 
                        "6ba85179e30d4fc2"
                    ]
                }
            }
        }
    ],
    "outbounds": [
        {
            "type": "direct",
            "tag": "direct"
        },
        {
            "type": "block",
            "tag": "block"
        }
    ]
}

# Define a function to replace the data
def replace_data(server, server_name):
    json_data['inbounds'][0]['tls']['server_name'] = server_name
    json_data['inbounds'][0]['tls']['reality']['handshake']['server'] = server
    return json_data

# Define a function to save the modified json data to a file
def save_to_file(data):
    with open('/root/sing-box_config.json', 'w') as file:
        json.dump(data, file)

# Define a function to handle the /replace command
def replace_handler(update, context):
    chat_id = update.message.chat_id
    text = update.message.text.split()
    if len(text) == 2:
        server = text[1]
        server_name = text[1]
        modified_data = replace_data(server, server_name)
        os.system('systemctl stop sing-box')
        save_to_file(modified_data)
        check = os.system('/root/sing-box check -c sing-box_config.json')
        if check == 0 :
            os.system('systemctl restart sing-box')
            os.system('systemctl start sing-box')
            context.bot.send_message(chat_id=chat_id, text="Data replaced successfully!")
        else:
            context.bot.send_message(chat_id=chat_id, text="Error in the json file")
    else:
        context.bot.send_message(chat_id=chat_id, text="Invalid command format. Usage: /replace server")

# Define the main function
def main():
    # Create a telegram bot and add a command handler for /replace command
    updater = Updater('telegram_bot_token_from_BotFather')
    updater.dispatcher.add_handler(CommandHandler('replace', replace_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
