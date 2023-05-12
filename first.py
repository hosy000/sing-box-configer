import pickle

user_data = {
    "user_id": "",
    "server_IP": "",
    "listen_port": 443,
    "bot_token": ""
}

user_data["server_IP"] = input("Enter server IP: ")
user_data["listen_port"] = int(input("Enter port number: "))
user_data["bot_token"] = input("Enter bot token: ")


with open("/root/user_data.pkl", "wb") as f:
    pickle.dump(user_data, f)
    print(f"-------user_data was created!-------\n{user_data}")
