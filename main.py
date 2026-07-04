from PIL import Image, ImageDraw, ImageFont
import textwrap

# قراءة القصة
with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()

# إنشاء صورة
img = Image.new("RGB", (1280, 720), color=(135, 206, 250))
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 42)
except:
    font = ImageFont.load_default()

text = "\n".join(textwrap.wrap(story, width=35))

draw.multiline_text(
    (60, 60),
    text,
    fill="black",
    font=font,
    spacing=10
)

img.save("thumbnail.png")

print("Thumbnail created successfully!")