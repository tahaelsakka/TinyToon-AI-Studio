import os
from huggingface_hub import InferenceClient
from PIL import Image

client = InferenceClient(
    provider="nscale",
    api_key=os.environ["HF_TOKEN"],
)

MODEL = "black-forest-labs/FLUX.1-schnell"


def load_story(filename="story.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
        def generate_image(prompt, output_file):
    image = client.text_to_image(
        prompt,
        model=MODEL,
    )

    image.save(output_file)
    return output_file


def create_prompt(scene):
    return f"""
A cute Pixar-style 3D cartoon for children.
Bright colors.
Soft lighting.
Happy facial expressions.
Ultra detailed.
No text.
Scene:
{scene}
"""