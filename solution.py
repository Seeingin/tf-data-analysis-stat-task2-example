import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 752592494

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import t

    alpha = 1 - p
    loc = np.mean(x)
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    t_value = t.ppf(1 - alpha / 2, df=len(x) - 1)
    interval = (loc - t_value * scale, loc + t_value * scale)
    return interval
