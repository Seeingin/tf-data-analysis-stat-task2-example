import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 752592494

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import t
    
    time = 56
    accelerations = (2 * x) / (time**2)
    mean_acceleration = accelerations.mean()
    standard_error = np.std(accelerations, ddof=1) / np.sqrt(len(accelerations))
    alpha = 1 - p
    t_score = t.ppf(1 - alpha / 2, df=len(accelerations) - 1)
    confidence_interval = (mean_acceleration - t_score * standard_error,
                           mean_acceleration + t_score * standard_error)
    return confidence_interval
