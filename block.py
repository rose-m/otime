from typing import List


class Block:
    """Describes a single block consisting of multiple choices
    """

    def __init__(self, p_values: List[float], t: int, k: int, n: int):
        """Create a new block consisting of multiple choices

        :param p_values: List with values of P to use per block
        :param t: Number of days until initial payout
        :param k: Number of days between initial and last payout (delay)
        :param n: Number of intermediate choices (apart from edge choices)
        """
        if type(p_values) is not list:
            raise ValueError("p_values must be a list, e.g. [1.05, 1.03]")
        if type(t) is not int or type(t) is not int or type(n) is not int:
            raise ValueError("parameters t, k, and n must be integers")
        if n < 0:
            raise ValueError("number of intermediate rounds n must be >= 0")

        self.p_values = p_values
        self.t = t
        self.k = k
        self.n = n

    def text_delay_start(self) -> str:
        """Returns a human readable text describing the start of the block (e.g. in 2 days) from today.

        :return: Human readable start of block from today
        """
        return self._days_to_text(self.t)

    def text_total_end(self) -> str:
        """Returns a human readable text describing the end of the block (e.g. in 6 weeks) from today.

        :return: Human readable end of block from today
        """
        return self._days_to_text(self.t + self.k)

    def questions(self) -> List['Question']:
        """Get the list of Questions described by this block

        :return: List of Questions
        """
        from .question import Question
        return [Question(self, i) for i in range(len(self.p_values))]

    @staticmethod
    def _days_to_text(value: int) -> str:
        """Interprets the given value as number of days in the future and returns a human readable presentation

        :param value: Number of days in the future
        :return: Human readable presentation
        """
        if value == 0:
            return "today"
        if value % 7 == 0:
            if value == 7:
                return "in 1 week"
            return "in {0:.0f} weeks".format(value / 7)
        if value == 1:
            return "in 1 day"
        return "in {0:.0f} days".format(value)
