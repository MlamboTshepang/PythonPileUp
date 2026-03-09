def main():
    A = [-3, 1, 2, -2, 5, 6]
    print(max_product(A))

def max_product(A):    
    max_product = A[0]
    for i in range(len(A)):        
        for j in range(i + 1, len(A)):
            max_product = max(max_product, A[i] * A[j])
    return max_product


if __name__ == "__main__":
    main()

# Mlambo Curations 2026 - Codility MaxProductOfThree Test Attempt