import asyncio, os, json
from prompt_gen import main_prompt, manimator


# returns path to the generated video
async def generate(user_prompt) -> tuple[str, str]:
    mp = main_prompt(user_prompt)
    code = manimator(mp)
    mp = mp[8:-4]
    print(mp)
    mp = json.loads(mp)
    mp = mp["text"]
    print(mp)
    code = code[10:-4]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "manim_script.py")
    with open(file_path, "w") as file:
        file.write(code)
    return (code, mp)
