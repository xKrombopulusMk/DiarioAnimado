from moviepy.editor import TextClip, concatenate_videoclips
from pathlib import Path


def create_cartoon(bullets: list[str], output_path: str) -> str:
    clips = []
    for b in bullets:
        clip = TextClip(b, fontsize=24, color='white', size=(640, 480)).set_duration(2)
        clips.append(clip)
    video = concatenate_videoclips(clips)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    video.write_videofile(str(path), fps=24)
    return str(path)
