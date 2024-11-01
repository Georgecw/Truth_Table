import pandas as pd
import numpy as np


def make_table(trues: list, dim: int, out_num: int):
    variables = []
    for i in range(0, dim):
        variables.append("A" + str(dim - i - 1))
    for j in range(0, out_num):
        variables.append("Y" + str(out_num - j - 1))

    data = np.zeros((2**dim, dim + out_num))
    for i in range(0, 2**dim):
        binary_str = bin(i)
        binary_list = list(str(binary_str))
        del binary_list[0:2]
        binary_arr = list(map(int, binary_list))
        for j in range(0, dim - len(binary_list)):
            binary_arr.insert(0, 0)
        binary_np = np.array(binary_arr)
        data[i] = np.hstack((binary_np, np.zeros(out_num)))

    table = pd.DataFrame(data=data, columns=variables, dtype=int)

    for out in range(0, out_num):
        table.iloc[trues[out], [dim + out]] = 1

    return table


# 录入数据
dim = int(input("请输入真值表的输入变量数: "))
out_num = int(input("请输入真值表的输出变量数: "))
trues = []
for i in range(1, out_num + 1):
    true_temp = input(
        "请输入第 " + str(i) + " 个输出变量中值为 1 的最小项, 用逗号分隔: "
    ).split(",")

    for i in range(len(true_temp)):
        true_temp[i] = int(true_temp[i])
        if true_temp[i] < 0 or true_temp[i] >= 2**dim:
            raise ValueError

    trues.append(true_temp)
    true_temp = []

# 制表并导出
table = make_table(trues, dim, out_num)
table.to_csv("Truth_Table.csv", index=False)
