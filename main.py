# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_matrix(matrix_to_print):
    str1 = ""
    for n in range(len(matrix_to_print)):
        str1 = str1 +"\n"+ str(matrix_to_print[n])
    return str1

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
    for r in range(size):
        maxi = abs(matrix[r][r])
        flag = 0
        for c in range(r, size):
            if abs(matrix[c][r]) > maxi:
                maxi = abs(matrix[c][r])
                flag = 1
                c_max = c
        if flag != 0:
            temp_matrix = exchange(r, c_max)
            mul = multiply_two_matrix(temp_matrix, mul)
            f1.writelines("-------------------------------------------------------")
            f1.writelines(f'{print_matrix(temp_matrix)}\nX{print_matrix(matrix)}\n=')
            matrix = multiply_two_matrix(temp_matrix, matrix)
            f1.writelines(f'{print_matrix(matrix)}\n')
    for r in range(size):
        for c in range(r, size):
            if matrix[r][r] == 1 and r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                f1.writelines("-------------------------------------------------------")
                f1.writelines(f'{print_matrix(temp_matrix)}\nX{print_matrix(matrix)}\n=')
                matrix = multiply_two_matrix(temp_matrix, matrix)
                f1.writelines(f'{print_matrix(matrix)}\n')
            else:
                temp_matrix = make_unit_matrix()
                if matrix[r][r] < 0:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                else:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                mul = multiply_two_matrix(temp_matrix, mul)
                f1.writelines("-------------------------------------------------------")
                f1.writelines(f'{print_matrix(temp_matrix)}\nX{print_matrix(matrix)}\n=')
                matrix = multiply_two_matrix(temp_matrix, matrix)
                f1.writelines(f'{print_matrix(matrix)}\n')
    for r in range(size-1, -1, -1):
        for c in range(r, -1, -1):
            if r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                f1.writelines("-------------------------------------------------------")
                f1.writelines(f'{print_matrix(temp_matrix)}\nX{print_matrix(matrix)}\n=')
                matrix = multiply_two_matrix(temp_matrix, matrix)
                f1.writelines(f'{print_matrix(matrix)}\n')
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
    f1 = open("file1.txt", 'w')
    f1.write(">>>Solution steps:>>>\n")
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
    f1.writelines("-------------------------------------------------------\n")
    f1.writelines(f'\nThe results are:')
    for n in range(len(final_result)):
        f1.writelines(f'\nX{n+1}={final_result[n]}')
    f1.close()
    print("<<<TO WATCH THE RESULTS GO CHECK FILE NAMED: file1>>>")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
