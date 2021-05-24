import random

def media(x_arr):
    return sum(x_arr) / len(x_arr)

if __name__ == '__main__':
    x_arr = [random.randint(1, 20) for _ in range (20)]
    mu = media(x_arr)
    print(x_arr)
    print(mu)
