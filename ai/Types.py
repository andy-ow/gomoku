from typing import NewType, Tuple

import numpy as np

GameState = NewType("GameState", np.ndarray)
Action = NewType("Action", Tuple[int,int])