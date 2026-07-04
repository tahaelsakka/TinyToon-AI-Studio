import os
from huggingface_hub import InferenceClient

MODEL = "black-forest-labs/FLUX.1-schnell"

client = InferenceClient(
    provider="nscale",
    api_key=os.environ["HF_TOKEN"],
)

def load_story(file_path="story.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def build_prompt(scene):
    return f"""
Cute Pixar style 3D cartoon.
Children animation.
Bright colors.
Happy faces.
Ultra detailed.
No text.
Scene:
{scene}
"""

def generate_image(prompt, output_path):
    image = client.text_to_image(
        prompt,
        model=MODEL,
    )

    image.save(output_path)
    def generate_all_images():
    scenes = load_story()

    if not scenes:
        print("No scenes found in story.txt")
        return

    os.makedirs("images", exist_ok=True)

    for i, scene in enumerate(scenes, start=1):
        filename = f"images/scene_{i}.png"

        print(f"Generating image {i}/{len(scenes)}")

        try:
            prompt = build_prompt(scene)
            generate_image(prompt, filename)
            print(f"Saved: {filename}")
        except Exception as e:
            print(f"Failed to generate image {i}: {e}")

    print("Image generation completed.")


if __name__ == "__main__":
    generate_all_images()