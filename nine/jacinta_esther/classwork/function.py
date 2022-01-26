def factorial(number):

    factorial_of_a_number = 1
    for i in range(1, number):
        factorial_of_a_number *= i
    return factorial_of_a_number


print(factorial(6))


def free_flow(a_string="--", an_int=0, a_float=0.0, a_list=[], a_dict={}):
    print(a_string)


free_flow(1, [2, 4, 6], 8.0)
