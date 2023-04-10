import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 752592494

#Асимптотический доверительный интервал
def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = (x.mean() + 0.5) / 1568.0
    scale = np.sqrt(np.var(x)) / (1568.0 * np.sqrt(len(x)))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)

#Точный доверительный интервал
def solution(p, x):
    alpha = 1 - p
    loc = (x.mean() - 0.5) / 1568.0
    scale = 1 / (1568.0 * len(x))
    return gamma.ppf(alpha / 2, len(x), loc=loc, scale=scale), \
           gamma.ppf(1 - alpha / 2, len(x), loc=loc, scale=scale)
