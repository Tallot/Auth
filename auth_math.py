import math

# Students ratio for t=13 and p=5%
student_table_ratio = 2.160


def expectancy(intervals):
    return sum(intervals) / len(intervals)


def dispersion(intervals, expect):
    return sum([(interv - expect) ** 2 for interv in intervals]) / (len(intervals) - 1)


def standard_deviation(disp):
    return math.sqrt(disp)


def student_s_ratio(intervals, expect, s_deviat):
    return math.fabs((intervals - expect) / s_deviat)


def student_empirical(intervals, interv):
    curr_intervals = [el for el in intervals if el != interv]
    curr_expectancy = expectancy(curr_intervals)

    student_empirical_ratio = student_s_ratio(
        intervals=curr_intervals,
        expect=curr_expectancy,
        s_deviat=standard_deviation(dispersion(curr_intervals, curr_expectancy))
    )
    return student_empirical_ratio


def intervals_filter(intervals):
    condition = True
    while condition:
        condition = False
        for interv in intervals:
            if student_empirical(intervals, interv) > student_table_ratio:
                intervals.remove(interv)
                condition = True
                break
