# Function to optimize budget allocation for a set of channels
# Given the total 'budget', coefficients 'coeff_A' for each channel, and channel names 'ch_names',
# this function uses the GEKKO optimization library to find an optimized budget allocation
# while considering upper-bound constraints for each channel. The function maximizes the value of
# the objective function based on coefficients and prints the budget allocation for each channel.

def optimize(budget, coeff_A, ch_names):
    # Import the GEKKO optimization library
    # Make sure to install GEKKO with 'pip install gekko' before using this function
    from gekko import GEKKO
    m = GEKKO()

    # Assign lower and upper bounds to each channel's budget allocation
    x1 = m.Var(lb=100, ub=budget)
    x2 = m.Var(lb=100, ub=budget)
    x3 = m.Var(lb=100, ub=budget)
    x4 = m.Var(lb=100, ub=budget)
    x5 = m.Var(lb=100, ub=budget)

    lst = []
    for j in range(5):
        print("Channel", j + 1, "should not exceed: ", end='')
        z = int(input())
        lst.append(z)

    # Apply upper-bound constraints to each channel
    m.Equation(x1 <= lst[0])
    m.Equation(x2 <= lst[1])
    m.Equation(x3 <= lst[2])
    m.Equation(x4 <= lst[3])
    m.Equation(x5 <= lst[4])

    # Ensure the total budget is not exceeded
    m.Equation(x1 + x2 + x3 + x4 + x5 <= budget)

    # Maximize the objective function based on coefficients
    m.Maximize(coeff_A[0] * x1 + coeff_A[1] * x2 + coeff_A[2] * x3 + coeff_A[3] * x4 + coeff_A[4] * x5)

    # Solve the optimization problem
    m.solve(disp=False)

    # Get the optimized budget allocation for each channel
    p1 = x1.value[0]
    p2 = x2.value[0]
    p3 = x3.value[0]
    p4 = x4.value[0]
    p5 = x5.value[0]

    # Print the budget allocation for each channel
    print('\n\nBudgets:\n\n')
    print(ch_names[0] + ": " + str(round(p1, 0)))
    print(ch_names[1] + ": " + str(round(p2, 0)))
    print(ch_names[2] + ": " + str(round(p3, 0)))
    print(ch_names[3] + ": " + str(round(p4, 0)))
    print(ch_names[4] + ": " + str(round(p5, 0)))
