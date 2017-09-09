def reverse(number):
    reversed_number = 0
    while number > 0:
        reversed_number *= 10
        reversed_number += number % 10
        number=number // 10
    return reversed_number

def is_palindrome(number):
    if number== reverse(number):
        print("input number is palindrome.")
    else:
        print("input number isn't palindrome.")
        
is_palindrome(99999)
is_palindrome(99991)
is_palindrome(99990)