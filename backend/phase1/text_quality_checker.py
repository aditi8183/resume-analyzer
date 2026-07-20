class TextQualityChecker:

    @staticmethod
    def is_valid_text(text):

        if not text:
            return False

        text = text.strip()

        if len(text) < 2:
            return False

        words = text.split()

        if not words:
            return False

        avg_word_len = (
            sum(len(word) for word in words)
            / len(words)
        )

        if avg_word_len > 25:
            return False

        return True