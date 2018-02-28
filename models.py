import json
import random
from typing import Optional, List

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

from .block import Block
from .config import BLOCKS

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'timepref'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    block_order = models.StringField(initial="")

    def creating_session(self):
        # TODO: create order of blocks for this subsession
        block_order = [i for i in range(len(BLOCKS))]
        random.shuffle(block_order)
        self.block_order = json.dumps(block_order)
        print(self.block_order)

    def get_block_order(self) -> List[int]:
        return json.loads(self.block_order)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    current_step = models.IntegerField(initial=0)
    block_answers = models.StringField(initial="")

    def goto_next_step(self):
        self.current_step = self.current_step + 1

    def get_current_step(self):
        return self.current_step

    def get_current_block_index(self) -> int:
        if self.current_step < len(BLOCKS):
            block_order = self.subsession.get_block_order()
            return block_order[self.current_step]
        else:
            return -1

    def get_current_block(self) -> Optional[Block]:
        block_index = self.get_current_block_index()
        if block_index >= 0:
            return BLOCKS[block_index]
        else:
            return None
