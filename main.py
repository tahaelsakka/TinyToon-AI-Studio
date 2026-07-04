from prompts import create_prompt

with open("story.txt", "r", encoding="utf-8") as f:
    scenes = [line.strip() for line in f if line.strip()]

print("=== TinyToon AI ===\n")

for i, scene in enumerate(scenes, 1):
    prompt = create_prompt(scene)

    print(f"Scene {i}")
    print(prompt)
    print("-" * 40)
    from make_video import *