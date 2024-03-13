class Matrix:
    """
      This was strutured to be a list in a list, in most of the case with a element->R but if element->C probably all the app fail.
      |1 2 3|
      |4 5 6| The system save it and operate it like [[1,2,3],[4,5,6],[7,8,9]]
      |7 8 9|
    """                                          
    def __init__(self):
        self.__my_matrix=list()
        self.__num_columns=0
        self.__num_rows=0

    def testMatrix1(self):
        self.__num_rows=2
        self.__num_columns=3
        self.__my_matrix=[[1,-1,-3],[0,-2,4]]

    def testMatrix2(self):
        self.__num_rows=3
        self.__num_columns=3
        self.__my_matrix=[[-1,-2,2],[0,1,3],[-3,2,0]]

    def testMatrix3(self):
        self.__num_rows=4
        self.__num_columns=4
        self.__my_matrix=[[-2,1,2,3],[0,-1,1,2],[-1,2,-2,1],[2,0,-1,4]]

    def testMatrix4(self):
        self.__num_rows=3
        self.__num_columns=3
        self.__my_matrix=[[-1,-2,2],[0,1,3],[-3,2,0]]

    def matrixGen(self,cant_rows,cant_columns,element):
        row_aux= list()                                
        self.__num_rows=cant_rows
        self.__num_columns=cant_columns

        for rows in range(0,cant_rows):
            for columns in range(0,cant_columns):
                row_aux.append(element)
            self.__my_matrix.append(row_aux)
            row_aux=list()

    def identityMatrix(self,cant):
        self.__num_rows=cant      
        self.__num_columns=cant
        row_aux=list()

        for rows in range(0,cant):
            for columns in range(0,cant):
               if(columns==rows):#then is a element of the main diagonal
                   row_aux.append(1)
               else:
                   row_aux.append(0)   
            self.__my_matrix.append(row_aux)
            row_aux=list()

    def inputMatrix(self,cant_rows,cant_columns):#this was thinked for only float valors!! 
        row_aux= list() 
        self.__num_rows=cant_rows
        self.__num_columns=cant_columns

        for rows in range(0,cant_rows):
            for columns in range(0,cant_columns):
              valor=float(input(f"elemento {columns} de la row:"))
              row_aux.append(valor)
            self.__my_matrix.append(row_aux)
            row_aux=list()

    def outputMatrix(self):
        for rows in range(0,self.__num_rows):
            print("|",end=" ")
            for columns in range(0,self.__num_columns):
                print(self.__my_matrix[rows][columns],end=" ")
            print("|")
        print("")
        """
        Examples:
        |1 2 3|

        |1|
        |2|
        |3|
        """
    def giveColumn(self)->int:
        return self.__num_columns
    
    def giveRow(self)->int:
        return self.__num_rows
    
    def mulbyScalar(self,constante):
        for columns in range(0,self.__num_columns):
            for rows in range(0,self.__num_rows):
                self.__my_matrix[columns][rows]= self.__my_matrix[columns][rows]*constante
        return self        

    def addition(self,matrix):#For two matrix each of same order nxm--- Σ i->n Σj->m(self[i,j]+matrix[i,j])
        for columns in range(0,self.__num_columns):
            for rows in range(0,self.__num_rows):
                self.__my_matrix[columns][rows]=matrix.__my_matrix[columns][rows]+self.__my_matrix[columns][rows]
        return self
    
    def subtraction(self,matrix):#a-b= a+(-1*b)
        matrix.mulbyScalar(-1)#(-1*b)
        self.addition(matrix)#a+(-1*b)
        return self
    
    def mulbetweenMatrixs(self,matrix):
        new_matrix=Matrix()
        if(self.__num_columns==matrix.__num_rows):#To A(self) of order nxm and B(matrix) of oxp, this operation only is available when m=o
            new_matrix.matrixGen(self.__num_rows,matrix.__num_columns,0)#A*B=C of order nxp and all the element are 0 because help to implement this calculation more easy

            for rows in  range(0,self.__num_rows):
                for columns in range(0,self.__num_columns):#remember m=o 
                    for second_columns in range(0,matrix.__num_columns):
                        element = new_matrix.__my_matrix[rows][second_columns]
                        element+=self.__my_matrix[rows][columns] * matrix.__my_matrix[columns][second_columns]#C[n,p]=C[n,p]+A[n,m]*B[o,p]
                        new_matrix.__my_matrix[rows][second_columns] =element    

            return new_matrix               

        else:
            print("invalid operation dosn't match columns of matrix1 with columns of matrix2")
            new_matrix.matrixGen(self.__num_rows,matrix.__num_columns,1)
            return new_matrix


    def matrixTranspose(self):
        new_matrix= Matrix()
        lista_aux = list() 
        for rows in range(0,self.__num_rows):
            for columns in range(0,self.__num_columns):
                if(rows==0):    
                    lista_aux.append(self.__my_matrix[rows][columns]) 
                    new_matrix.__my_matrix.append(lista_aux)
                    lista_aux=list()
                else:
                    new_matrix.__my_matrix[columns].append(self.__my_matrix[rows][columns])
            
        new_matrix.__num_columns=self.__num_rows
        new_matrix.__num_rows=self.__num_columns  
      
        return new_matrix       
    
    def adj(self,i,j):
        adj_value=0
        matrix_ij =Matrix()
        matrix_ij.matrixGen(self.__num_rows-1,self.__num_columns-1,0)
        aux_rows =0
        aux_columns=0

        for rows in range(0,self.__num_rows):
            for columns in range(0,self.__num_columns):
                if(rows!=i and columns!=j):
                    matrix_ij.__my_matrix[aux_rows][aux_columns]=self.__my_matrix[rows][columns]
                    aux_columns+=1
                    if(aux_columns>=matrix_ij.__num_columns):
                        aux_rows+=1
                        aux_columns=0  

        adj_value=((-1)**((i)+(j)))*matrix_ij.det()


        return adj_value

    def det(self):
        det_value=0
        if(self.__num_columns==self.__num_rows and self.__num_columns>0):
            if(self.__num_columns==1):
                det_value=self.__my_matrix[0][0]
            else:
                for columns in range(0,self.__num_columns):# A(aij)  Det A= a_i1*Adj_i1 + a_i2*Adj_i2 + .... + a_in*Adj_in
                    det_value+=self.__my_matrix[0][columns]*self.adj(0,columns)
        else:
            print("Not available opertation, det=0  for keep running the program")

        return det_value
    def adjMatrix(self):
        new_matrix=Matrix()
        new_matrix.matrixGen(self.__num_columns,self.__num_columns,0)
        aux_matrix= self.matrixTranspose()
        for rows in range(0,self.__num_rows):
            for columns in range(0,self.__num_columns):
                new_matrix.__my_matrix[rows][columns]=aux_matrix.adj(rows,columns)

        return new_matrix
    
    def invMatrix(self):
        new_matrix=Matrix()
        det_a = self.det()
        if(det_a!=0):
                new_matrix =self.adjMatrix()*(1/det_a)
        return new_matrix
    def __add__(self, matrix):
        return self.addition(matrix)
    
    def __sub__(self,matrix):
        return self.subtraction(matrix)
    
    def __mul__(self,element):
        if(type(element)!=Matrix):
            return self.mulbyScalar(element)
        else:
            return self.mulbetweenMatrixs(element)
    

        
second_matrix=Matrix()
new_matrix= Matrix()

second_matrix.testMatrix2()
new_matrix =second_matrix.invMatrix()
new_matrix.outputMatrix()
thirdmatrix=second_matrix*new_matrix
thirdmatrix.outputMatrix()

"""
new_matrix.testMatrix3()
new_matrix.outputMatrix()
val =new_matrix.det()
print(val)
new_matrix.testMatrix1()
second_matrix.testMatrix2()
new_matrix=new_matrix*second_matrix
new_matrix.outputMatrix()
new_matrix.inputMatrix(2,2)
new_matrix.outputMatrix()
second_matrix.matrixGen(2,2,0)
second_matrix+=new_matrix
second_matrix.outputMatrix()
second_matrix-= new_matrix
second_matrix.outputMatrix()
new_matrix.inputMatrix(3,3)
new_matrix.outputMatrix()
second_matrix=new_matrix.matrixTranspose()
second_matrix.outputMatrix()
new_matrix=second_matrix.matrixTranspose()
new_matrix.outputMatrix()

"""
