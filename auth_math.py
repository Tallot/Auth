import math


def expectancy(interv):
    return sum(interv) / len(interv)


def dispersion(interv_s, expect):
    return sum([interv - expect for interv in interv_s]) / (len(interv_s) - 1)


def standard_deviation(disp):
    return math.sqrt(disp)


def student_s_ratio(interv, expect, s_deviat):
    return math.fabs()