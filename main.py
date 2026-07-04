with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()

scenes = story.split(".")

print("Scenes:\n")

for i, scene in enumerate(scenes):
    scene = scene.strip()
    if scene:
        print(f"Scene {i+1}: {scene}")