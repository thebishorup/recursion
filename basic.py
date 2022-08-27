def print_name(i , n):
    # base case
    if i > n:
        return
    
    print(f"John: {i}")
    
    print_name(i + 1, n)
    
def print_backtracking(i, n):
    # base case
    if i > n:
        return
    
    print_backtracking(i + 1, n)
    
    print(i)
    
def parameter_sum(n, sum):
    # base case
    if n < 1:
        print(sum)
        return
    
    parameter_sum(n - 1, sum + n)
    
def functional_sum(n):
    if n == 0:
        return 0
    
    return n + functional_sum(n - 1)
    
# execution
#print_name(1, 10)
#print_backtracking(1, 4)
#parameter_sum(3, 0)
print(functional_sum(3))