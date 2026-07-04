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
            final_video = concatenate_videoclips(clips, method="compose")

    final_video.write_videofile(
        "output.mp4",
        fps=24,
        codec="libx264",
        audio=False,
    )

    print("Video created successfully.")


if __name__ == "__main__":
    make_video()