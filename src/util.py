import numpy as np

def moving_average(values: np.ndarray, smooth: float):
    if smooth < 0.0 or smooth > 1.0:
        raise ValueError(f"smooth must be in [0, 1], but got {smooth}")
    n = int((1.0 - smooth) * 1 + smooth * len(values))
    ret = np.cumsum(values, dtype=float)
    ret[n:] = (ret[n:] - ret[:-n]) / n
    ret[:n] = ret[:n] / np.arange(1, n + 1)
    return ret