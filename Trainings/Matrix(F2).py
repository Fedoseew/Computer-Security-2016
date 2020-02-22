bool=1
while bool!=0:
    print('Введите размерность матрицы: ')
    print()
    n=int(input())
    def setMatrix(n):
        global m
        m=[]
        for i in range(n):
            print('Введите элементы', i, 'строки матрицы (через пробел):')
            global matrix
            matrix=input()
            matrix = matrix.split(' ')
            m.append(matrix)
        for i in range(len(m)):
            for j in range(len(m[i])):
                m[i][j]=int(m[i][j])%2
        for i in range(len(m)):
            for j in range(len(m[i])):
                print(m[i][j], end=' ')
            print()
        print()
        global dim
        dim = len(m)
    def det(m):
        res = 1
        n = len(m)
        for i in range(n):
            # выбираем опорный элемент
            j = max(range(i,n), key=lambda k: abs(m[k][i]))
            if i != j:
                m[i],m[j] = m[j],m[i]
                res *= -1
            # убеждаемся, что матрица не вырожденная
            if m[i][i] == 0:
                return 0
            res *= m[i][i]
            # "обнуляем" элементы в текущем столбце
            for j in range(i+1,n):
                b = m[j][i] / m[i][i]
                m[j] = [m[j][k]-b*m[i][k] for k in range(n)]
        print("Определитель матрицы равен= ", res)
        return res

    setMatrix(n)
    det(m)
    print()
    print("Для продолжения нажмите 1/ Для выхода нажмите 0: ")
    bool=int(input())