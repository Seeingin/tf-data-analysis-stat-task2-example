import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 752592494

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    time = 56
    accelerations = (2 * x) / (time**2)
    mean_acceleration = accelerations.mean()
    standard_error = np.std(accelerations, ddof=1) / np.sqrt(len(accelerations))
    confidence_interval = (mean_acceleration + standard_error * norm.ppf(alpha / 2),
                           mean_acceleration + standard_error * norm.ppf(1 - alpha / 2))
    return confidence_interval
