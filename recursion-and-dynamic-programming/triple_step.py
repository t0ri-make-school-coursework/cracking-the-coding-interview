# 8.1
# Triple Step
# A child is running up a staircase with n steps and can either hop
# 1 step, 2 steps, or 3 stops at a time. Implement a method to count
# how many possible ways the child can run up the stairs.

def step_up(steps):
    if steps < 0:
        return 0
    if steps is 0:
        return 1
    else:
        return step_up(steps - 1) + step_up(steps - 2) + step_up(steps - 3)

if __name__ == "__main__":
    print(step_up(3))
    # 1 step three times
    # 1 step twice, 2 steps once
    # 3 steps once
    # 2 steps once, 1 step once
    print(step_up(10))