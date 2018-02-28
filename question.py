from .config import TOTAL_BUDGET


class Question:
    def __init__(self, block, index):
        self.block = block
        self.index = index
        self.num_choices = block.n + 2
        self.p = self.block.p_values[self.index]

    def question_number(self):
        return self.index + 1

    def start_values(self):
        start = round(TOTAL_BUDGET / self.p, 2)
        unrounded = [(self.num_choices - 1 - i) * start / (self.num_choices - 1) for i in range(self.num_choices)]
        return [round(v, 1) for v in unrounded]

    def end_values(self):
        unrounded = [i * TOTAL_BUDGET / (self.num_choices - 1) for i in range(self.num_choices)]
        return [round(v, 1) for v in unrounded]

    def choice_index(self):
        return range(1, self.num_choices + 1)
