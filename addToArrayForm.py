from time import time

def addToArrayForm_1st(A, K):
    last_ptr = -1
    while K != 0:
        k = K % 10
        K //= 10
        
        if last_ptr == -len(A) - 1:
            A = [k] + A
            last_ptr -= 1
            continue
            
        A[last_ptr] += k
        mem_ptr = last_ptr
        last_ptr -= 1
        
        while A[mem_ptr] > 9:
            A[mem_ptr] -= 10
            mem_ptr -= 1
            if mem_ptr == -len(A) - 1:
                A = [1] + A
                break
            else:
                A[mem_ptr] += 1
    return A

def addToArrayForm_2nd(A, K):
    A_num = ''
    for num in A:
        A_num += str(num)
    A_num = int(A_num) + K
    return [c for c in str(A_num)]

A = [1,2,3,4,1]
K = 512962

start = time()
addToArrayForm_1st(A, K)
end = time()

print(end - start)

start = time()
addToArrayForm_2nd(A, K)
end = time()

print(end - start)