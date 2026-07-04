from moviepy import ImageClip, concatenate_videoclips

images = []

for image in images:
    clip = ImageClip(image).with_duration(3)

print("Video module ready")