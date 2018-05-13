import math


Fisher_standard = 2.48 #Fisher coefficient for 14x14 freedom levels
Student_standard = 2.145 #Student coefficient for 14 freedom levels
K_e = 3

# Students ratio for t=13 and p=5%
student_table_ratio = 2.160


def expectancy(intervals):
    return sum(intervals) / len(intervals)


def dispersion(intervals, expect):
    return sum([(interv - expect) ** 2 for interv in intervals]) / (len(intervals) - 1)


def standard_deviation(disp):
    return math.sqrt(disp)


def student_s_ratio(interv, expect, s_deviat):
    return math.fabs((interv - expect) / s_deviat)


def intervals_checker(intervals, interv):
    curr_intervals = [el for el in intervals if el != interv]
    curr_expectancy = expectancy(curr_intervals)

    student_empirical_ratio = student_s_ratio(
        interv=interv,
        expect=curr_expectancy,
        s_deviat=standard_deviation(dispersion(curr_intervals, curr_expectancy))
    )

    if student_empirical_ratio > student_table_ratio:
        return False
    else:
        return True


def intervals_filter(intervals):
    condition = True
    while condition:
        for interv in intervals:
            if not intervals_checker(intervals, interv):
                intervals.remove(interv)
                condition = True
                break


def dispersions_uniformity_check(S1, S2):
    S_max = max(S1, S2)
    S_min = min(S1, S2)
    Fisher_coef = S_max/S_min
    
    return Fisher_coef < Fisher_standard


def hyphothesis_check(auth_times, standard_times):
    n = len(auth_times)
    M_x_lambda = sum(standard_times)/n
    M_y = sum(auth_times)/n
    
    S_x_lambda = sum([(x - M_x_lambda)**2 for x in standard_times])/(n-1)
    S_y = sum([(y - M_y)**2 for y in auth_times])/(n-1)
    
    S = math.sqrt( (S_x_lambda**2 + S_y**2)*(n-1) / (2*n-1) )
    t_p = math.fabs((M_x_lambda - M_y) / (S*math.sqrt(2/n)))
    
    return t_p < Student_standard