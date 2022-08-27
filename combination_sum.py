def combination_sum(index, combination, sub_seq, sum, k):
    if index >= len(combination):
        if sum is k:
            print(sub_seq)
        return
            
    sub_seq.append(combination[index])
    sum += combination[index]
    combination_sum(index + 1, combination, sub_seq, sum, k)
    
    sub_seq.remove(combination[index])
    sum -= combination[index]
    combination_sum(index + 1, combination, sub_seq, sum, k)
    
numbers = [2,3,6,7]
combination_sum(0, numbers, [], 0, 7)