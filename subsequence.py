def print_subsequences(index, sub_seq, sequence):
    if index >= len(sequence):
        print(f'{sub_seq} -> {len(sub_seq)}')
        return
    
    sub_seq.append(sequence[index])
    print_subsequences(index + 1, sub_seq, sequence)
    
    #remove from sub_seq
    sub_seq.remove(sequence[index])
    print_subsequences(index + 1, sub_seq, sequence)
    
numbers = 'apl'
print_subsequences(0, [], numbers)