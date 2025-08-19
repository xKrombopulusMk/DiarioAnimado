from gtts import gTTS
from pathlib import Path


def synthesize(text: str, output_path: str) -> str:
    tts = gTTS(text=text, lang="pt")
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tts.save(path)
    return str(path)
