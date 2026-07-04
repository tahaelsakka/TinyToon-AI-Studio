import glob
from moviepy import ImageClip, concatenate_videoclips


def make_video():
    images = sorted(glob.glob("images/*.png"))

    if not images:
        print("No images found.")
        return

    clips = []

    for image in images:
        clip = ImageClip(image).with_duration(4)
        clips.append(clip)