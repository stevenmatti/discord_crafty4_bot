import requests
from dotenv import load_dotenv
import os

load_dotenv() # reads variables from a .env file and sets them in os.environ



# Crafty 4 api token
crafty_api_token    = os.getenv('CRAFTY_TOKEN') 

server_ip           = os.getenv('SERVER_IP')
server_port         = os.getenv('SERVER_PORT')
minecraft_server_id = os.getenv('MINECRAFT_SERVER_ID')

#url = f"https://{server_ip}:{server_port}/api/v2/servers/{minecraft_server_id}/action/start_server"

headers = {
    "Authorization": f"Bearer {crafty_api_token}",
    "Content-Type": "application/json"
}

# Only commands to get send to crafty api
minecraftServerActions = {"start_server", "stop_server"}


def minecraft_server_commands(action="none"):
    print(f"action: {action}")

    # Loop over minecraftServerActions to check if passed action is within the valid ones in the arry
    if action not in minecraftServerActions:
        print(f"ERROR: action '{action}' is NOT valid !!")
        return


    url = f"https://{server_ip}:{server_port}/api/v2/servers/{minecraft_server_id}/action/{action}"
    print(f"Running action {action} on Minecraft Server")
    response = requests.post(url, headers=headers, verify=False)
    
    print(response.status_code)
    print(response.text)


# Main function gets called if this was ran
# instead of being imported as a module
def main():
    minecraft_server_commands("stop_server")

# This will be for testing the crafty api for minecraft server
# when ran with `python file.py`
if __name__ == "__main__":
    main()
