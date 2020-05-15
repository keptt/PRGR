import xlrd
import pulp


def solve_all(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, u1min, u1max, u2min, u2max
                , y1min, y1max, y3min, y3max, y4min, y4max, y5min, y5max, y7min, y7max, y11min, y11max, y16min, y16max):
    model = pulp.LpProblem('min_problem', pulp.LpMinimize)

    u1 = pulp.LpVariable('u1', lowBound=u1min, upBound=u1max, cat='Continuous')
    u2 = pulp.LpVariable('u2', lowBound=u2min, upBound=u2max, cat='Continuous')


    model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107)
    # model += 34.2376 + x6*(-0.00145696) + x16*0.000694627 + u2*(-2.54756), 'f6'

    model += 48.1197 + x1*u1*(-0.000747192) + x1**2*0.00613734 + x10*u1*0.000618299 >= y1min
    model += 48.1197 + x1*u1*(-0.000747192) + x1**2*0.00613734 + x10*u1*0.000618299 <= y1max

    model += -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05) >= y3min
    model += -1.53931 + x1*0.0281138 + x3*u1*0.00413477 + x14*u1*(-2.98551e-05) <= y3max

    model += -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831 >= y4min
    model += -0.884918 + x4*u2*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831 <= y4max

    model += -45.0064 + x5*x8*0.00240169 + u1*1.12033 + u1*x8*(-0.00361076) >= y5min
    model += -45.0064 + x5*x8*0.00240169 + u1*1.12033 + u1*x8*(-0.00361076) <= y5max

    model += 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999) >= y7min
    model += 24.2162 + x5*x11*0.000320931 + x7*u2*0.0791588 + u1*(-0.112999) <= y7max

    model += -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369 >= y11min
    model += -12.6811 + x2*17.5335 + x7*u1*(-0.000768576) + x11*u2*0.0899369 <= y11max

    # model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107) >= y16min
    # model += 32.7168 + x6*u1*(-1.12157e-05) + x16*x15*5.76132e-06 + u2*(-2.42107) <= y16max

    model.solve()

    print('-' * 20)
    print(pulp.LpStatus[model.status])

    u1_res = u1.varValue
    u2_res = u2.varValue

    print('U1 = {}'.format(u1_res))
    print('U2 = {}'.format(u2_res))

    y16_minimized = abs(float(pulp.value(model.objective)))
    print()
    print('Y16 = {}'.format(y16_minimized))
    print()

    print('Y1 = {}'.format(48.1197 + x1*u1_res*(-0.000747192) + x1**2*0.00613734 + x10*u1_res*0.000618299))
    print('Y3 = {}'.format(-1.53931 + x1*0.0281138 + x3*u1_res*0.00413477 + x14*u1_res*(-2.98551e-05)))
    print('Y4 = {}'.format(-0.884918 + x4*u2_res*0.0615484 + x5*x13*(-0.000378937) + x6*x7*0.000919831))
    print('Y5 = {}'.format(-45.0064 + x5*x8*0.00240169 + u1_res*1.12033 + u1_res*x8*(-0.00361076)))
    print('Y6 = {}'.format(24.2162 + x5*x11*0.000320931 + x7*u2_res*0.0791588 + u1_res*(-0.112999)))
    print('Y7 = {}'.format(-12.6811 + x2*17.5335 + x7*u1_res*(-0.000768576) + x11*u2_res*0.0899369))


def main():
    file_path = 'our_dataset_new_raw.xlsx'
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)

    arr = []

    for i in range(1, 26):
        arr = sheet.row_values(i)
        # print(*arr[1:17], 100, 200, 12, 13, arr[19] - 10, arr[19] + 10, arr[21] - 2, arr[21] + 2, arr[22] - 2, arr[22] + 2, arr[23] - 2, arr[23] + 2, arr[25] - 2, arr[25] + 2, arr[29] - 2, arr[29] + 2, arr[34] - 1, arr[34] + 2)
        # solve_all(*arr[1:17]
        # , 50, 400, 10, 14, 82, 112, 1, 5.5, 50, 150, 60, 120, 60, 130, 60, 140, 0.1, 5.5)


        solve_all(*arr[1:17], 50, 400, 10, 14, 82, 112, 1, 50000.5, 50, 150, 60, 120, 60, 130, 60, 140, 0.1, 5.5)


if __name__ == '__main__':
    main()
