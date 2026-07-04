from PIL import Image, ImageDraw

img = Image.new("RGB", (1280, 720), color="skyblue")
draw = ImageDraw.Draw(img)

draw.text((350, 330), "TinyToon AI Studio", fill="black")

img.save("thumbnail.png")

print("Thumbnail created successfully!")