class Quote:
    def __init__(self, quote, answer, value):
        self.type_ = "quote"
        self.quote = quote
        self.answer = answer
        self.value = value
        self.asked = False
