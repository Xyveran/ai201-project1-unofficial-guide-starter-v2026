import re


def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects or not answer:
        return False

    expected_words = set(re.findall(r"\b\w+\b", expects.lower()))
    answer_words = set(re.findall(r"\b\w+\b", answer.lower()))

    return expected_words <= answer_words
