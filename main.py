from PIL import Image, ImageDraw

with open("story.txt", "r") as f:
    story = f.readlines()

for i, line in enumerate(story):
    img = Image.new("RGB", (1280, 720), color="skyblue")
    draw = ImageDraw.Draw(img)

    draw.text((80, 300), line.strip(), fill="black")

    img.save(f"scene_{i+1}.png")

print("Scenes created successfully!")