import pandas as pd
import numpy as np

from scipy.stats import norm
#from scipy.stats import chi2


chat_id = 1056349463 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return (-(x.mean() * np.sqrt(len(x))) / (norm.ppf(alpha / 2) * np.sqrt(31)), -(x.mean() * np.sqrt(len(x))) / (norm.ppf(1 - alpha / 2) * np.sqrt(31)))
