import random
import moviepy.editor as mp
from gtts import gTTS
from PIL import Image, ImageDraw

# STEP 1 — Generate an idea automatically
ideas = [
    "3 facts about space",
    "Motivational quote about success",
    "The future of AI",
    "Top 3 productivity tips",
    "A powerful mindset lesson"
]

topic = random.choice(ideas)
print("AI topic:", topic)

# STEP 2 — Generate script
script = f"Did you know? {topic}. Follow for more powerful content."

# STEP 3 — Generate voice
tts = gTTS(script)
tts.save("voice.mp3")

# STEP 4 — Generate simple image
img = Image.new("RGB", (1080,1920), color=(20,20,20))
draw = ImageDraw.Draw(img)
draw.text((100,900), topic, fill=(255,255,255))
img.save("image.png")

# STEP 5 — Create video
image_clip = mp.ImageClip("image.png").set_duration(5)
audio_clip = mp.AudioFileClip("voice.mp3")

video = image_clip.set_audio(audio_clip)
video.write_videofile("tiktok_video.mp4", fps=24)

print("Video created: tiktok_video.mp4")
