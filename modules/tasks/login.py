import requests
from modules.write.write import write

async def login_attempt():

    headers = {
        "Host": "api.gencraft.com",
        "Connection": "keep-alive",
        "Content-Length": "94",
        "X-Csrf-Protection":"1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-WEB-TOKEN": "YOURWEBTOKENHERE (WILL AUTOMATE THIS AT A LATER DATE)",
        "Origin": "https://gencraft.com",
        "Referer": "https://gencraft.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    '''
    "first_name": "your google account firstname", 
    "last_name": "your google account lastname",
    "auth_provider": "google",
    "timezone": "America/New_York" #or your timezone   
    '''

    data = {
    "first_name": "John", 
    "last_name": "Doe",
    "auth_provider": "google",
    "timezone": "America/New_York"
    }

    login_request = requests.post("https://api.gencraft.com/api/v5/user/login", headers=headers, json=data, timeout=20)

    if "SESSION_ID" in login_request.cookies:
    # Get the value of the "SESSION_ID" cookie
        session_id = login_request.cookies["SESSION_ID"]
    else:
        write("SESSION_ID cookie not found in the response.", 'error')

    if login_request.status_code == 200:
        return session_id
    else:
        return 'False'