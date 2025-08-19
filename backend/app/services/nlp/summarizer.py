def summarize_events(events: list[dict]) -> list[str]:
    """Stub summarizer: returns event contents as bullet points."""
    bullets = []
    for ev in events:
        content = ev.get("content")
        if isinstance(content, str):
            bullets.append(content)
        else:
            bullets.append(str(content))
    return bullets
