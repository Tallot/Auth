import math

# Students ratio for t=13 and p=5%
student_table_ratio = 2.160


def expectancy(intervals):
    return sum(intervals) / len(intervals)


def dispersion(intervals, expect):
    return ((sum([interv - expect for interv in intervals])) ** 2) / (len(intervals) - 1)


def standard_deviation(disp):
    return math.sqrt(disp)


def student_s_ratio(intervals, expect, s_deviat):
    return math.fabs((intervals - expect) / s_deviat)


def intervals_filter(intervals):
    for interv in intervals:
        curr_intervals = [el for el in intervals if el != interv]
        curr_expectancy = expectancy(curr_intervals)

        student_empirical_ratio = student_s_ratio(
            intervals=curr_intervals,
            expect=curr_expectancy,
            s_deviat=standard_deviation(dispersion(curr_intervals, curr_expectancy))
        )

        if student_empirical_ratio > student_table_ratio:
            intervals.remove()
