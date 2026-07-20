class ConfidenceScorer:

    @staticmethod
    def pdf_confidence():
        return 1.0

    @staticmethod
    def ocr_confidence(ocr_result):

        scores = []

        for line in ocr_result:
            try:
                scores.append(line[1][1])
            except Exception:
                pass

        if not scores:
            return 0.0

        return round(sum(scores) / len(scores), 4)