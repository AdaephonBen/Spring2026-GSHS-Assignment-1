# Sample change

def grad_f(x, y):
    df_dx = 2*x + 2
    df_dy = 2*y + 4
    return df_dx, df_dy

def gradient_descent(starting_values, learning_rate, num_iterations):
    x, y = starting_values
    for _ in range(num_iterations):
        df_dx, df_dy = grad_f(x, y)
        x -= learning_rate * df_dx
        y -= learning_rate * df_dy
    return x, y
