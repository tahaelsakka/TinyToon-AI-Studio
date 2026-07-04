 from prompts import create_prompt

def generate_images(story_file="story.txt"):
    with open(story_file, "r", encoding="utf-8") as f:
        scenes = [line.strip() for line in f if line.strip()]

    prompts = []

    for i, scene in enumerate(scenes, 1):
        prompt = create_prompt(scene)
        prompts.append(prompt)

        print(f"Image {i}")
        print(prompt)
        print("-" * 40)

    return prompts


if __name__ == "__main__":
    generate_images()