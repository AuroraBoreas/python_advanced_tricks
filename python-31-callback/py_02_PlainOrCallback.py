from __future__ import print_function

def fibonacci():
    values = []
    while True:
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]
        if values[-1] > 100:
            print(values)
            break

if __name__ == "__main__":
    fibonacci()