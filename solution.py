import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1056349463 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    t_value = t.ppf(1 - alpha/2, len(x)-1)
    left = np.sqrt(len(x)*np.var(x)/t_value**2)
    right = np.sqrt(len(x)*np.var(x)/t_value**2)
    return (loc - left, loc + right)
