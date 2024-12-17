import sys
import os
import numpy as np
import multi

def Test(iteration)-> float:
    result = 0.0
    for _ in range(iteration):
        Dimensions = np.random.randint(1, 101, 3)
        A = np.random.randint(0, 100, (Dimensions[0], Dimensions[1]))
        B = np.random.randint(0, 100, (Dimensions[1], Dimensions[2]))
        C = np.dot(A, B)  
        D = multi.matrix_multiply(A, B)
        if(np.array_equal(C, D)):
            result+=1
        else:
            print(C)
            print(D)
    return 100 * result / iteration

def main()-> None:
    print(Test(1000))

if __name__ == ("__main__"):
    main()