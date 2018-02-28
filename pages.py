from ._builtin import Page, WaitPage
from .config import BLOCKS


class BlockPage(Page):
    form_model = 'player'
    form_fields = ['block_answers']

    def is_displayed(self):
        return self.player.get_current_block() is not None

    def vars_for_template(self):
        step = self.player.get_current_step() + 1
        block_index = self.player.get_current_block_index() + 1
        current_block = self.player.get_current_block()
        num_blocks = len(BLOCKS)
        return {
            'step': step,
            'block_index': block_index,
            'num_blocks': num_blocks,
            'progress': round(step * 100 / num_blocks),
            'curr_block': current_block
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_step()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


def generate_page_sequence():
    return [BlockPage] * len(BLOCKS) + [ResultsWaitPage, Results]


page_sequence = generate_page_sequence()