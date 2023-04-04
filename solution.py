import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 752592494

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    mean = x.mean()
    standard_error = np.std(x, ddof=1) / np.sqrt(len(x))
    z = norm.ppf(1 - alpha / 2)
    confidence_interval = (mean - z * standard_error, mean + z * standard_error)
    return confidence_interval
