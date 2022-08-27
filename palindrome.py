def is_palindrome(sentence, left, right):
    if left >= right:
        return
    
    if sentence[left] is not sentence[right]:
        return False
    
    is_palindrome(sentence, left + 1, right - 1)
    
    return True

sentence = 'madame'
print(is_palindrome(sentence, 0, len(sentence) - 1))