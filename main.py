# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def make_unit_matrix():
    unit_matrix = []
    for i in range(0, size):
        temp = []

        for j in range(0, size):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        unit_matrix.append(temp)
    return unit_matrix

def make_elementary_matrix(pivot, num1, row, col):
    temp_elementary = make_unit_matrix()
    temp_elementary[row][col] = -1 * (num1 / pivot)
    return temp_elementary

def exchange(row, row_replace):
    unit_matrix = temp_elementary = make_unit_matrix()
    temp_elementary[row], temp_elementary[row_replace] = unit_matrix[row_replace], unit_matrix[row]
    return temp_elementary


def gauss_method(matrix):
    mul = make_unit_matrix()
    """open a file"""
    for r in range(size):
        maxi = abs(matrix[r][r])
        flag = 0
        for c in range(size):
            if abs(matrix[r][c]) > maxi:
                maxi = abs(matrix[r][c])
                flag = 1
                c_max = c
        if flag != 0:
            temp_matrix = exchange(r, c_max)
            mul = multiply_two_matrix(temp_matrix, mul)
            print(mul)
            """print the multiply to a file"""
            matrix = multiply_two_matrix(temp_matrix, matrix)
    for r in range(size):
        for c in range(r, size):
            if matrix[r][r] == 1:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                """print the multiply to a file"""
                print(mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
            else:
                temp_matrix = make_unit_matrix()
                if matrix[r][r] < 0:
                    temp_matrix[r][r] = -1 / matrix[r][r]
                else:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                mul = multiply_two_matrix(temp_matrix, mul)
                print(mul)
                """print the multiply to a file"""
                matrix = multiply_two_matrix(temp_matrix, matrix)

    for r in range(size-1, -1, -1):
        for c in range(r, -1, -1):
            if r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                print(mul)
                """print the multiply to a file"""
                matrix = multiply_two_matrix(temp_matrix, matrix)
    return mul


def multiply_two_matrix(matrix1, matrix2):
    result = []
    for r in range(len(matrix1)):
        helper_res = []
        for c in range(len(matrix1)):
            helper_res.append(0)
        result.append(helper_res)
    for i in range(len(matrix1)):
        # iterating by column by B
        for j in range(len(matrix2[0])):
            # iterating by rows of B
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = []
    answer_matrix = []
    final_result = []
    size = int(input("Enter size of the matrix n >> (nXn): "))
    for i in range(size):
        helper = []
        for j in range(size):
            num = float(input(f'matrix[{i}][{j}]='))
            helper.append(num)
        matrix.append(helper)
        num = float(input(f'result num in row {i + 1}='))
        answer_matrix.append(num)
    multiply_elementary_matrix = gauss_method(matrix)
    for i in range(size):
        final_result.append(0)
    for r in range(len(multiply_elementary_matrix)):
        for c in range(len(multiply_elementary_matrix)):
            final_result[r] += multiply_elementary_matrix[r][c] * answer_matrix[c]
    print(final_result) #צריך להדפיס לאא בצורת מטריצה אלא בצורת משתנים X,Y,Z

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
