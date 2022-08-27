def combination_sum_II(index, combinations, sub_seq, k):
    #base case
    if index >= len(combinations):
        if k == 0:
            print(sub_seq)
        return
            
    if combinations[index] <= k:
        sub_seq.append(combinations[index])
        combination_sum_II(index, combinations, sub_seq, k - combinations[index])
        sub_seq.remove(sub_seq[len(sub_seq) - 1])
        
    combination_sum_II(index + 1, combinations, sub_seq, k)
 
numbers = [2,3,6,7]
combination_sum_II(0, numbers, [], 7)