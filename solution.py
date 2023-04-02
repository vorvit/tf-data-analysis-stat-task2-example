import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 1056349463 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    sample_mean = np.mean(x)
    sample_var = np.var(x, ddof=1)  # ddof=1 используется для расчета несмещенной выборочной дисперсии
    alpha = 1 - p
    chi2_left = chi2.ppf(alpha/2, n-1)
    chi2_right = chi2.ppf(1-alpha/2, n-1)
    left = np.sqrt((n-1)*sample_var/chi2_right)/0.31
    right = np.sqrt((n-1)*sample_var/chi2_left)/0.31
    return (sample_mean - left, sample_mean + right)
