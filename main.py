import time
import asyncio
import requests

from modules.write.write import write
from modules.tasks.login import login_attempt
from modules.tasks.generateImage import generate_image


async def start():
    loginRequest = await login_attempt()
    if loginRequest == 'False':
        write("There was a problem logging in.", "error")
    else:
        write(f"Session ID: {loginRequest}", 'info')

    await generate_image(loginRequest)

if __name__ == "__main__":
   asyncio.run(start())