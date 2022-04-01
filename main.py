"""С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
//////////////////////////////////////////////////////////////////////////////////////////////////////
Формируется матрица F следующим образом: если в С количество простых чисел в нечетных столбцах в области 2 больше,
чем количество нулевых  элементов в четных строках в области 3, то поменять в С симметрично области 1 и 3 местами,
иначе С и В поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: ((К*A)*F– (K * AT) . Выводятся по мере формирования А, F и все
матричные операции последовательно."""


import random
import time

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return True

def print_matrix(M, matr_name, tt):
    print("Матрица " + matr_name + ". Промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()


print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100: "))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100: "))
    K = int(input("Введите число К = "))
    start = time.time()
    A, F, AF, AT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        AT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):  # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10 , 10)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
         for j in range(row_q):
             F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []  # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):  # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)

    q_prime = 0
    q_zero = 0
    for i in range(size):  # обрабатываем подматрицу С
        for j in range(i + 1, size, 1):
            if j % 2 == 1 and j > size - 1 - i and IsPrime(C[i][j]):
                q_prime += 1
            elif j % 2 == 0 and C[i][j] == 0 and j < size - 1 - i:
                q_zero += 1

    print("Количество простых чисел в нечетных столбцах в области 2: ", q_prime, "Количество нулевых  элементов в четных строках в области 3: ", q_zero)

    if q_prime > q_zero:
        for i in range(size // 2, size, 1):  # меняем подматрицу С
            for j in range(0, i, 1):
                C[i][j], C[i][size - j - 1] = C[i][size - j - 1], C[i][j]
        for i in range(1, size // 2, 1):
            for j in range(0, i, 1):
                C[i][j], C[i][size - j - 1] = C[i][size - j - 1], C[i][j]
        print_matrix(C, "C", time_next - time_prev)
        for i in range(size):  # формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = C[i][j]
    else:
        for i in range(row_q // 2):
            for j in range(0, row_q // 2):
                F[i][j], F[i][row_q // 2 + row_q % 2 + j] = F[i][row_q // 2 + row_q % 2 + j], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):  # K*A
        for j in range(row_q):
            A[i][j] = K * A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A", time_next - time_prev)

    for i in range(row_q):  # (K*A)*F
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            AF[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "(K*A) * F", time_next - time_prev)

    for i in range(row_q):  # AT
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):  # K*AT
        for j in range(row_q):
            AT[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A*F^T", time_next - time_prev)

    for i in range(row_q):  # ((К*A)*F– (K * AT)
        for j in range(row_q):
            AF[i][j] = AF[i][j] - AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "((К * A) * F – (K * AT)", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")
except ValueError:
     print("\nЭто не число.")
except FileNotFoundError:
     print(
         "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")