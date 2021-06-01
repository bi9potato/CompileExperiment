import numpy as np


def precede_function():

    precede_stable = np.array([['>', '<', '<', '>', '<', '>'],
                               ['>', '>', '<', '>', '<', '>'],
                               ['<', '<', '<', '=', '<', ''],
                               ['>', '>', '', '>', '', '>'],
                               ['>', '>', '', '>', '', '>'],
                               ['<', '<', '<', '', '<', '=']])

    precede_function = np.ones((2, 6), dtype=np.int)

    flag = True
    while (flag):
        flag = False
        for i in range(precede_stable.shape[0]):
            for j in range(precede_stable.shape[1]):
                if (precede_stable[i, j] == '>'):
                    if (precede_function[0, i] <= precede_function[1, j]):
                        precede_function[0, i] = precede_function[1, j] + 1
                        flag = True
                elif (precede_stable[i, j] == '<'):
                    if (precede_function[0, i] >= precede_function[1, j]):
                        precede_function[1, j] = precede_function[0, i] + 1
                        flag = True
                elif (precede_stable[i, j] == '='):
                    if (precede_function[0, i] != precede_function[1, j]):
                        precede_function[1, j] = precede_function[0, i] = precede_function[0, i] if precede_function[0, i] > precede_function[1, j] else precede_function[1, j]
                        flag = True
        # print('\n',precede_function)

    # print('优先函数：\n', precede_function)

    return precede_function
