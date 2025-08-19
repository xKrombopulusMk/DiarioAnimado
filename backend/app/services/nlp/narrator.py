import random


def narrate(bullets: list[str], style: str = "poetic") -> str:
    if style == "poetic":
        return "\n".join(f"📝 {b}" for b in bullets) + "\nQue jornada!"
    if style == "funny":
        jokes = ["haha", "lol", "rs"]
        return " ".join(bullets) + " - " + random.choice(jokes)
    return " ".join(bullets)
