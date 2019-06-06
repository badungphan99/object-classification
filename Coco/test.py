from collections import Counter
import matplotlib.pyplot as plt

def test():
    a = [25, 25, 1, 1, 4, 2, 3, 7, 7, 8, 23]
    a.sort()
    recounter = Counter(a)

    print(recounter)
    x = [*recounter.keys()]
    y = [*recounter.values()]
    print(x)
    print(y)
    len_x = len(x)

    num_cols = 3

    max_x = x[len_x - 1]

    new_x = []

    new_y = []

    temp = int(max_x / num_cols)

    for i in range(num_cols):
        new_x.append(temp * i)
    new_x.append(max_x)

    for i in range(1, len(new_x)):
        temp_y = 0
        for j in range(len(y)):
            if x[j] > new_x[i - 1] and x[j] <= new_x[i]:
                temp_y += y[j]

        new_y.append(temp_y)
    new_x.remove(new_x[0])
    print(new_x)
    print(new_y)
    tuple(new_x)

    plt.bar(new_x, new_y, align='center')  # A bar chart
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    for i in range(len(new_y)):
        plt.hlines(new_y[i], 0, new_x[i])
    plt.show()

if __name__ == "__main__":

    test()
    # xv = (8,16,25)
    # yv = (8,0,3)
    # print(type(xv))
    # plt.bar(xv, yv, align='center')  # A bar chart
    # plt.xlabel('Bins')
    # plt.ylabel('Frequency')
    # for i in range(len(yv)):
    #     plt.hlines(yv[i], 0, xv[i])  # Here you are drawing the horizontal lines
    # plt.show()
