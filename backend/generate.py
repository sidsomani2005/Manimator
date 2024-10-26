import asyncio


# returns path to the generated video
async def generate(prompt: str) -> str:
    await asyncio.sleep(5)
    return "./output/GTTSExample.mp4"
