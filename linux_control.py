import subprocess
import requests
import time, os

# Replace with your bot token and base URL
bot_token = "take this from bot Father"
bot_token = os.getenv('BOT_TOKEN_LINUX') # this is comming from env variable
base_url = f"https://api.telegram.org/bot{bot_token}"

def send_message(chat_id, text):
    url = f"{base_url}/sendMessage"
    params = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

def execute_command(command):

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=10)
        response = f"Command executed successfully:\n```\n{output.decode('utf-8')}\n```"
    except subprocess.CalledProcessError as e:
        response = f"Command failed with error:\n```\n{e.output.decode('utf-8')}\n```"
    except subprocess.TimeoutExpired:
        response = "Command timed out."
    return response

def handle_message(command, chat_id):
    
    # Execute the command received from the user
    response = execute_command(command)

    # Send the response back to the user
    send_message(chat_id, response)

def main():
    # Run the bot indefinitely, listening for messages
    # welcome
    welcome_mess = "Welcome My Friend. You can control Linux Server using Command. Any time you can exit by typing 100"
    send_message(2143134192, welcome_mess)
    epoch_time = int(time.time())
    old_messege_id = 0
    while True:
        try:
            update = requests.get(f"{base_url}/getUpdates").json()
            messege_id = update["result"][-1]["message"]["message_id"]
            if update["ok"] and update["result"]:
                if update["result"][-1]["message"]["date"] > epoch_time:
                    if messege_id != old_messege_id:
                        # print(update["result"])
                        # print(update["result"][-1]["message"]["date"])
                        # print(update["result"][-1]["message"]["text"])
                        chat_id = update["result"][-1]["message"]["chat"]["id"]
                        old_messege_id = messege_id
                        # print(messege_id, old_messege_id)
                        # chat_id = update["message"]["chat"]["id"]
                        command = update["result"][-1]["message"]["text"].strip()
                        # print("command is ", command)
                        actualcommand = command[0].lower()+ command[1:]
                        print("Typed command is--> ", actualcommand)
                        if actualcommand == "100":
                            last_messege = "Thank you for using these services. Bye Have a good day"
                            send_message(chat_id, last_messege)
                            exit("Thank you for using this services")
                        # print(chat_id)
                        handle_message(actualcommand, chat_id)
        except Exception as e:
            print(f"Error occurred: {e}")

        time.sleep(1)


if __name__ == '__main__':
    # Start the main loop
    main()
