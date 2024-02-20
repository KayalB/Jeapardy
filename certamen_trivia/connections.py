class Connection:
    def __init__(self, s1, s2, s3, s4, answer, value):
        self.type_ = "connection"
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.answer = answer
        self.value = value
        self.asked = False
