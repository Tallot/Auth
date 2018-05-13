import math

Fisher_standard = 2.48 #Fisher coefficient for 14x14 freedom levels
Student_standard = 2.145 #Student coefficient for 14 freedom levels
K_e = 3

def expectancy(interv):
    return sum(interv) / len(interv)


def dispersion(interv_s, expect):
    return sum([interv - expect for interv in interv_s]) / (len(interv_s) - 1)


def standard_deviation(disp):
    return math.sqrt(disp)


def student_s_ratio(interv, expect, s_deviat):
    return math.fabs((interv - expect) / s_deviat)

    
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
    
