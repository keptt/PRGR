import xlrd
import pulp


def solve_all(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, u1min, u1max, u2min, u2max
                , y1min, y1max, y3min, y3max, y4min, y4max, y5min, y5max, y7min, y7max, y11min, y11max, y16min, y16max):
    model = pulp.LpProblem('min_problem', pulp.LpMinimize)

    u1 = pulp.LpVariable('u1', lowBound=u1min, upBound=u1max, cat='Continuous')
    u2 = pulp.LpVariable('u2', lowBound=u2min, upBound=u2max, cat='Continuous')

    # print('x5: ', x5)
    # print(y5min, y5max)
    # print(u1min, u1max)
    # print(u2min, u2max)




    # model += -28.4902 + x5*u1*0.00215669 + u1*x8*0.0812971 + x8**2*(-0.000302408), 'F6'
    # model += -26.6274 + x5*0.468269 + u1*0.409352 + x8*(-0.0937273), 'F6'
    # model += -45.0064 + x5*x8*0.00240169 + u1*1.12033 + u1*x8*(-0.00361076)
    # model += -26.6274 + x5*0.468269 + u1*0.409352 + x8*(-0.0937273)

    # model += -4.77716 + x1*1.15132 + x1*u1*(-0.000766655) + x10*u1*0.000579103 >= y1min
    # model += -4.77716 + x1*1.15132 + x1*u1*(-0.000766655) + x10*u1*0.000579103 <= y1max

    # model += -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05) >= y3min
    # model += -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05) <= y3max

    # model += -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831 >= y4min
    # model += -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831 <= y4max

    # model += -28.4902 + x5*u1*0.00215669 + u1*x8*0.0812971 + x8**2*(-0.000302408) >= y5min
    # model += -28.4902 + x5*u1*0.00215669 + u1*x8*0.0812971 + x8**2*(-0.000302408) <= y5max

    # model += 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999) >= y7min
    # model += 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999) <= y7max

    # model += -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369 >= y11min
    # model += -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369 <= y11max


    # model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107) >= y16min
    # model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107) <= y16max





    # model += -45.0064 + X5*X8*0.00240169 + U1*1.12033 + U1*X8*(-0.00361076)
    model += -4.77716 + x1*1.15132 + x1*u1*(-0.000766655) + x10*u1*0.000579103, 'F6'

    model += 48.1197 + x1*u1*(-0.000747192) + x1**2*0.00613734 + x10*u1*0.000618299 >= y1min
    model += 48.1197 + x1*u1*(-0.000747192) + x1**2*0.00613734 + x10*u1*0.000618299 <= y1max

    model += -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05) >= y3min
    model += -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05) <= y3max

    model += -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831 >= y4min
    model += -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831 <= y4max

    # model += -28.4902 + x5*u1*0.00215669 + u1*x8*0.0812971 + x8**2*(-0.000302408) >= y5min
    # model += -28.4902 + x5*u1*0.00215669 + u1*x8*0.0812971 + x8**2*(-0.000302408) <= y5max

    model += 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999) >= y7min
    model += 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999) <= y7max

    model += -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369 >= y11min
    model += -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369 <= y11max

    model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107) >= y16min
    model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107) <= y16max

    model.solve()
    print(pulp.LpStatus[model.status])

    print("U1 = {}".format(u1.varValue))
    print("U2 = {}".format(u2.varValue))

    print('Y5 = {}'.format(pulp.value(model.objective)))


def main():
    file_path = 'our_dataset_new_raw.xlsx'
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)

    arr = []

    for i in range(1, 26):
        arr = sheet.row_values(i)
        # print(*arr[1:17], 100, 200, 12, 13, arr[19] - 10, arr[19] + 10, arr[21] - 2, arr[21] + 2, arr[22] - 2, arr[22] + 2, arr[23] - 2, arr[23] + 2, arr[25] - 2, arr[25] + 2, arr[29] - 2, arr[29] + 2, arr[34] - 1, arr[34] + 2)
        solve_all(*arr[1:17], 50, 400, 10, 14, 82, 112, 1, 5.5, 50, 150, 60, 120, 60, 130, 60, 140, 0.8, 3.8)


if __name__ == '__main__':
    main()
