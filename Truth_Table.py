import pandas as pd
import numpy as np


def make_table(trues, dim):
    dim = int(dim)

    variables = []
    for i in range(0, dim):
        variables.append("A" + str(i))
    variables.append("Y")

    data = np.zeros((2**dim, dim + 1))
    for i in range(0, 2**dim):
        bi = bin(i)
        bi_arr = list(str(bi))
        del bi_arr[0:2]
        bi_arr = [int(bi) for bi in bi_arr]
        for j in range(0, dim - len(bi_arr)):
            bi_arr.insert(0, 0)
        bi_arr.append(0)
        bi_np = np.array(bi_arr)
        data[i] = bi_np

    table = pd.DataFrame(data=data, columns=variables, dtype=int)

    table.iloc[trues, [dim]] = 1

    return table


dim = int(input("请输入真值表的输入变量数: "))
trues = input("请输入值为 1 的最小项, 用逗号分隔: ").split(",")
trues = [int(num) for num in trues]
table = make_table(trues, dim)
table.to_csv("Truth_Table.csv", index=False)
