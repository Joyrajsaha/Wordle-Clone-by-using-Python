class LetterPosition:
    def __init__(self, ch: str):
        self.ch: str = ch
        self.is_in_word: bool = False
        self.is_in_position: bool = False

    def __repr__(self):
        return f"[{self.ch} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}]"
