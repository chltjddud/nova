def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
        
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 30
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}") # 결과 1: 30번째 피보나치 수 출력
    
    n_large = 100
    result_large = fibonacci(n_large)
    print(f"The {n_large}th Fibonacci number is: {result_large}") # 결과 2: 100번째 피보나치 수 출력
