import asyncio, os, json, subprocess
from speech_gen import (
    final_flow,
    remove_code_block_markers,
    error_checking_agent,
    video_checking_agent,
)


async def generate_video() -> tuple[str, str]:
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
        "manim_voiceover_image",  # Ensure this matches the built image name
        "manim",
        "-pql",
        "/manim/manim_script.py",
        "--disable_caching",
    ]

    process = subprocess.run(
        docker_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    stdout = process.stdout.decode("utf-8")
    stderr = process.stderr.decode("utf-8")

    if process.returncode != 0:
        print(f"Error running Manim script:\n{stderr}")
        return ("", stderr)

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
    return (video_path, "")
    # return "./backend/output/GTTSExample.mp4"


# returns path to the generated video
async def generate(
    user_prompt, replaceCode=None, reuseMetadata=None
) -> tuple[str, str]:
    if replaceCode is None or reuseMetadata is None:
        metadata, code = final_flow(user_prompt)
    else:
        metadata = reuseMetadata
        code = replaceCode

    metadata_json = json.loads(remove_code_block_markers(metadata))

    # steps = metadata_json["steps"]
    # transcript = ""
    # for step in steps:
    #     if steps[step] is not None:
    #         transcript += steps[step] + "\n\n"
    # transcript = transcript[:-2]

    transcript = metadata_json["srt"]

    code = remove_code_block_markers(code, language="python")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "manim_script.py")
    with open(file_path, "w") as file:
        file.write(code)
    print("Manim script generated.")
    print(metadata_json)
    video_path, err_msg = await generate_video()
    print(video_path, err_msg)
    if video_path == "" and err_msg != "":
        print(f"Error generating video: {err_msg}")
        print("Regenerating code...")
        newCode = error_checking_agent(
            subject=metadata_json["title"], code=code, err=err_msg
        )
        print("New code generated. Regenerating video...")
        return await generate(user_prompt, replaceCode=newCode, reuseMetadata=metadata)
    else:
        # review the videa for quality assurance
        video_path = video_checking_agent(video_path, metadata_json)
    return (code, transcript, video_path)


# if __name__ == "__main__":
#     asyncio.run(generate("explain division"))
#     asyncio.run(generate_video())
