import time
import requests
import json

from modules.write.write import write

async def generate_image(sessionId):
    time.sleep(2)

    cookies = {
    'SESSION_ID': f'{sessionId}',
    }

    headers = {
        'authority': 'api.gencraft.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://gencraft.com',
        'referer': 'https://gencraft.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
        'x-csrf-protection': '1',
    }

    '''
    model styles
    art_style 1 = 3D Style
    art_style 2 = Anime Style
    art_style 14 = CyberPunk Style
    art_style 9 = Realistic Style
    art_style 29 = Video Game Style
    art_style 17 = Isometric Style
    
    '''

    json_data = {
        'prompt_text': 'A blue and gold macaw chilling on a tree overviewing the rainforest', #Give model a custom prompt here
        'art_style_id': 9,
        'negative_prompt_text': '',
        'media_type': 'image',
        'model_id': 1,
        'width': 1024,
        'height': 1024,
    }

    generate_image_request = requests.post('https://api.gencraft.com/api/v5/prompt/generate', cookies=cookies, headers=headers, json=json_data, timeout=30)
    json_data = generate_image_request.text

    json_obj = json.loads(json_data)

    image_urls = []
    if "data" in json_obj and "images" in json_obj["data"]:
        images = json_obj["data"]["images"]
        for image in images:
            if "url" in image:
                image_urls.append(image["url"])

    for url in image_urls:
        write(f"Image Generated: {url}", "success")
