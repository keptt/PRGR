import xlrd
import itertools
from pprint import pprint


def float_intersect(first, second, precision=0.001):
    sort_key = lambda elem : list(elem.values())[0]

    first.sort(key=sort_key)
    second.sort(key=sort_key)

    intersect = []

    for i in first:
        k_i, v_i = tuple(i.items())[0]
        start = 0

        for j in itertools.islice(second, start, None):
            k_j, v_j = tuple(j.items())[0]

            if is_close(v_i[0], v_j[0], precision) and is_close(v_i[1], v_j[1], precision):
                intersect.append({k_i : v_i})
            elif v_i[0] < v_j[0]:
                break
            else:
                start += 1

    return intersect


def is_close(source, target, precision=0.001):
    return abs(source - target) <= precision


def solve_all(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, u1min, u1max, u2min, u2max, y1min, y1max, y3min, y3max, y4min, y4max, y5min, y5max, y7min, y7max, y11min, y11max, y16min, y16max):
    u1 = 0
    u2 = 0

    y1_arr = []
    y3_arr = []
    y4_arr = []
    y5_arr = []
    y7_arr = []
    y11_arr = []
    y16_arr = []


    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y1 = 48.1197 + x1*u1*(-0.000747192) + x1**2*0.00613734 + x10*u1*0.000618299
            if y1 >= y1min and y1 <= y1max:
                y1_arr.append({y1 : (u1, u2)})
            u2 += 0.1
            # print(len(y1_arr))


    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y3 = -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05)
            if y3 >= y3min and y3 <= y3max:
                y3_arr.append({y3 : (u1, u2)})
            u2 += 0.1
            # print(len(y3_arr))

    # a = []
    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y4 = -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831
            # a.append(y4)
            if y4 >= y4min and y4 <= y4max:
                y4_arr.append({y4 : (u1, u2)})
            u2 += 0.1
            # print(len(y4_arr))
    # pprint(sorted(a))

    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y5 = -28.4902 + x5*u1*0.00215669 + u1*x8*0.0812971 + x8**2*(-0.000302408)
            if y5 >= y5min and y5 <= y5max:
                y5_arr.append({y5 : (u1, u2)})
            u2 += 0.1
    # pprint(y5_arr)


    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y7 = 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999)
            if y7 >= y7min and y7 <= y7max:
                y7_arr.append({y7 : (u1, u2)})
            u2 += 0.1
            # print(len(y7_arr))


    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y11 = -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369
            if y11 >= y11min and y11 <= y11max:
                y11_arr.append({y11 : (u1, u2)})
            u2 += 0.1
            # print(len(y11_arr))


    for u1 in range(u1min, u1max + 1, 1):
        u2 = u2min
        while u2 <= u2max:
            y16 = 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107)
            # if y16 >= y16min and y16 <= y16max:
            y16_arr.append({y16 : (u1, u2)})
            u2 += 0.1

    # pprint(sorted(y16_arr, key=lambda elem : list(elem.keys())[0], reverse=True))

    precision = 0.1
    print('y1_arr: ', len(y1_arr))
    print('y3_arr: ', len(y3_arr))
    print('y4_arr: ', len(y4_arr))
    print('y5_arr: ', len(y5_arr))
    print('y7_arr: ', len(y7_arr))
    print('y11_arr: ', len(y11_arr))
    print('y16_arr: ', len(y16_arr))

    # res = float_intersect(y1_arr, y3_arr, precision)
    # pprint(y4_arr)
    # print(res)
    res = float_intersect(y1_arr, y4_arr, precision)
    res = float_intersect(res, y7_arr, precision)
    res = float_intersect(res, y11_arr, precision)
    res = float_intersect(res, y16_arr, precision)

    # print(x16)
    # print(y16min, y16max)

    res = float_intersect(res, y5_arr, precision)

    # result_value = max(res) if res else None

    # print(result_value)

    pprint(sorted(res, key=lambda elem : list(elem.keys())[0], reverse=True))


def main():
    file_path = 'our_dataset_new_raw.xlsx'
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)

    arr = []
    # sheet.cell_value(0, 0)
    for i in range(1, 2):#(1, 2):#27):
        arr = sheet.row_values(i)

        # print(*arr[1:17], 100, 200, 12, 13, arr[19] - 10, arr[19] + 10, arr[21] - 2, arr[21] + 2, arr[22] - 2, arr[22] + 2, arr[23] - 2, arr[23] + 2, arr[25] - 2, arr[25] + 2, arr[29] - 2, arr[29] + 2, arr[34] - 1, arr[34] + 2)

        solve_all(*arr[1:17], 100, 200, 12, 13, arr[19] - 10, arr[19] + 10, arr[21] - 2, arr[21] + 2, arr[22] - 10, arr[22] + 10, arr[23] - 2, arr[23] + 2, arr[25] - 2, arr[25] + 2, arr[29] - 2, arr[29] + 2, arr[34] - 1, arr[34] + 2)


if __name__ == '__main__':
    main()
    # a = [{6.504061820000001: (200, 12.999999999999996)}]
    # b = {6.504061820000001: (200, 12.999999999999996)}]
