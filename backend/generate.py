import asyncio, os, json
from prompt_gen import main_prompt, manimator


# returns path to the generated video
async def generate(user_prompt) -> tuple[str, str]:
    mp = main_prompt(user_prompt)
    code = manimator(mp)
    mp = mp[8:-4]
    mp = json.loads(mp)
    mp = mp["text"]
    code = code[10:-4]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "manim_script.py")
    with open(file_path, "w") as file:
        file.write(code)
    return (code, mp)


async def generate_video():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    script_path = os.path.join(output_dir, "manim_script.py")

    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Manim script not found at {script_path}")

    docker_command = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{output_dir}:/manim",
        "manim_voiceover_image",  # Use the custom image
        "manim",
        "-pql",
        "/manim/manim_script.py",
        "--disable_caching",
    ]

    process = await asyncio.create_subprocess_exec(
        *docker_command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        error_message = stderr.decode()
        print(f"Error running Manim script:\n{error_message}")
        raise RuntimeError("Manim script failed to run.")

    media_dir = os.path.join(output_dir, "media", "videos", "manim_script")

    if not os.path.exists(media_dir):
        raise FileNotFoundError("Media directory not found after rendering.")

    resolutions = [
        d for d in os.listdir(media_dir) if os.path.isdir(os.path.join(media_dir, d))
    ]
    if not resolutions:
        raise FileNotFoundError("No resolution directories found after rendering.")

    resolution_dir = os.path.join(media_dir, resolutions[0])

    video_files = [f for f in os.listdir(resolution_dir) if f.endswith(".mp4")]

    if not video_files:
        raise FileNotFoundError("No video files found after rendering.")

    video_file = video_files[0]
    video_path = os.path.join(resolution_dir, video_file)

    # return video_path
    # return video_path
    return "./backend/output/GTTSExample.mp4"


if __name__ == "__main__":
    # asyncio.run(generate("Visually explain of how matrix transformations work"))
    asyncio.run(generate_video())
