class Block:
    def __init__(self, p_values, t: int, k: int, n: int):
        """
        Describes a single block consisting of multiple choices
        :param p_values: Tuple with values of P to use per block
        :param t: Number of days until initial payout
        :param k: Number of days between initial and last payout (delay)
        :param n: Number of intermediate choices (apart from edge choices)
        """
        if not (type(p_values) is tuple or type(p_values) is list):
            raise ValueError("p_values must be a tuple or a list, e.g. (1.05, 1.03) or [1.05, 1.03]")
        if not type(t) is int or not type(t) is int or not type(n) is int:
            raise ValueError("parameters t, k, and n must be integers")
        if n < 0:
            raise ValueError("number of intermediate rounds n must be >= 0")

        self.p_values = p_values
        self.t = t
        self.k = k
        self.n = n

    def text_delay_start(self):
        return self._days_to_text(self.t)

    def text_total_end(self):
        return self._days_to_text(self.t + self.k)

    def questions(self):
        from .question import Question
        return [Question(self, i) for i in range(len(self.p_values))]

    @staticmethod
    def _days_to_text(value: int):
        if value == 0:
            return "today"
        if value % 7 == 0:
            if value == 7:
                return "in 1 week"
            return "in {0:.0f} weeks".format(value / 7)
        if value == 1:
            return "in 1 day"
        return "in {0:.0f} days".format(value)
