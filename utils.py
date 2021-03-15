import math
import numpy as np


def murray_law(diameter_p, diameter_1):
    """
    :param diameter_p: parent diameter
    :param diameter_1: diameter of first node
    :return: diameter of second node
    """
    diameter_2 = math.pow(math.pow(diameter_p, 3) - math.pow(diameter_1, 3), 1 / 3)
    return diameter_2


def gauess_distribute(u, sig):
    def gauess_value(x):
        y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
        return y_sig

    return gauess_value


def exponential_distribute(lmd):
    def exponential_value(x):
        return lmd * np.exp(-lmd * x)

    return exponential_value
