from __future__ import print_function

def fibonacci():
    values = []
    while True:
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]
        # when fibonacci numbers are wholly divided by 17...
        if not values[-1] % 17:
            print(values[-1])
        # when finonacci numbers are greater than 10000 ...
        if values[-1] > 10_000:
            # print(values)
            break

if __name__ == "__main__":
    fibonacci()