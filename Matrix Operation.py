class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix_A = [i[:] for i in [[0]*self.col]*self.row]
        self.matrix_B = [i[:] for i in [[0]*self.col]*self.row]
        self.matrix_C = [i[:] for i in [[0]*self.col]*self.row]


    def getinp(self, mat):
        for i in range(self.row):
            for j in range(self.col):
                mat[i][j] = int(input(f'Enter the element of row {i+1} and column {j+1}: '))

    def printmat(self, mat):
        for i in mat:
            print('\t'.join(map(str, i)))

    def getmatrix(self):
        print('\n\nEnter Matrix A data: ')
        self.getinp(self.matrix_A)

        print('\nEnter Matrix B data: ')
        self.getinp(self.matrix_B)

        print('\n\nMatrix A')
        self.printmat(self.matrix_A)

        print('\nMatrix B')
        self.printmat(self.matrix_B)


    def addition(self):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix_C[i][j] = self.matrix_A[i][j] + self.matrix_B[i][j]

        print("\n\nAddition matrix: ")
        self.printmat(self.matrix_C)


    def subtraction(self):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix_C[i][j] = self.matrix_A[i][j] - self.matrix_B[i][j]

        print("\n\nSubtraction matrix: ")
        self.printmat(self.matrix_C)


    def multiply(self):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix_C[i][j] = 0
                for k in range(self.row):
                    self.matrix_C[i][j] += self.matrix_A[i][k] * self.matrix_B[k][j]

        print("\n\nMultiplication matrix: ")
        self.printmat(self.matrix_C)


    def transpose(self):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix_C[i][j] = self.matrix_A[j][i]

        print("\n\nTranspose of Matrix A: ")
        self.printmat(self.matrix_C)

        for i in range(self.row):
            for j in range(self.col):
                self.matrix_C[i][j] = self.matrix_B[j][i]

        print("\n\nTranspose of Matrix B: ")
        self.printmat(self.matrix_C)

def main():
    row = int(input('\nEnter number of rows: '))
    col = int(input('Enter number of columns: '))
    mat = Matrix(row, col)
    mat.getmatrix()
    mat.addition()
    mat.subtraction()
    mat.multiply()
    mat.transpose()

if __name__ == "__main__":
    main()
