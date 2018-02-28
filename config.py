"""
This file includes all available configuration options for the timepref app.

Modify this file to set all your preferences - it's not suggested to edit any of the other files.
"""

from .block import Block

#: The total budget available for each choice
TOTAL_BUDGET = 20

#: Set to True if you want blocks to be randomized in order
RANDOMIZE_BLOCKS = False

#: The configuration for all blocks to be displayed to the user
BLOCKS = [
    Block(
        p_values=(1.05, 1.10, 1.15, 1.20),
        t=0,
        k=35,
        n=4
    ),
    Block(
        p_values=(1.10, 1.03),
        t=5,
        k=35,
        n=4
    )
]
