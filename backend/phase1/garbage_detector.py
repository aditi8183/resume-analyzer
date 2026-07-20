import re


class GarbageDetector:

    @staticmethod
    def is_garbage(text):

        if not text:
            return True

        text = text.strip()

        if len(text) < 2:
            return True

        cleaned = re.sub(
            r"[A-Za-z0-9\s\.\,\-\+\#\/]",
            "",
            text
        )

        ratio = len(cleaned) / max(len(text), 1)

        return ratio > 0.5