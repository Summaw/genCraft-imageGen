![image](https://github.com/Summaw/genCraft-imageGen/assets/98126132/996b03cb-6038-4718-8e18-fe3bdf6d20b7)

# genCraft-imageGen
A basic python tool to automate the process of generating images at `https://gencraft.com`

# Prompt
- You can change the prompt you would like to give it here: [HERE](modules/tasks/generateImage.py#L37)
- I will add an input line that will ask you for your prompt.

# How To Use
- You will need to get your X-WEB-TOKEN from the initial request to register/login.
- You can use dev tools and get it from the network tab it will be in the request headers for this url: `https://api.gencraft.com/api/v5/user/login`
- You will get the value from that header and place it here: [HERE](modules/tasks/login.py#L14C9-L14C9)
- Once you have done that and saved the updated file you should be able to successfully sign into your account. That token should be valid for 24 hours.

# Models to choose from
- art_style 1 = 3D Style
- art_style 2 = Anime Style
- art_style 14 = CyberPunk Style
- art_style 9 = Realistic Style
- art_style 29 = Video Game Style
- art_style 17 = Isometric Style

# Output
- Generated responses will be output to data folder in generated.json.
- Response example below:

```json
[
    {
        "prompt": {
            "prompt_text": "A blue and gold macaw chilling on a tree overviewing the rainforest",
            "art_style_id": 9
        },
        "urls": [
            "https://image.gencraft.com/",
            "https://image.gencraft.com/",
            "https://image.gencraft.com/"
        ]
    }
]
```

# Potential Updates at 20 stars!
- Automatic account generation with google
- Maybe a gui to see images generated
- Premium features supported
- Bot examples (telegram/discord)
- A web page containing all information and generated images with prompts and keys.
