def solution(A, B, K):
    A = int(A)
    B = int(B)
    K = int(K)
    for i in range(B):
        if(A<=B):
            diff = B - A
            Answer = int(diff % K)
            print(Answer)
            print("is divisible x amount of times")
        else:
            print("incorrect")

if __name__ == "__main__":
    print("Please enter the first number")
    A = input()
    print("Please enter the Second number")
    B = input()
    print("Please enter the Dividing number")
    K = input()
    
    solution(A,B,K)
#Mlambo Curationsa 2026 Codility Tests - CountDiv attempt