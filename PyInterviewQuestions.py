# 1.Fibonacci Sequence:
# Write a function to generate the Fibonacci sequence up to a specified number of terms.

def fibonacci_iterative(n):
    # Handle edge cases
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n + 1):
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series

# Test the function
print(fibonacci_iterative(10))



def is_palindrome_builtin(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
print(is_palindrome_builtin("A man a plan a canal Panama"))  # True
print(is_palindrome_builtin("Hello"))  # False


def is_palindrome_manual(s):
    # Convert to lowercase and remove spaces manually
    cleaned_str = ""
    for char in s:
        if char != " ":
            cleaned_str += char.lower()
    
    # Compare the original string with the reversed string
    length = len(cleaned_str)
    for i in range(length // 2):
        if cleaned_str[i] != cleaned_str[length - 1 - i]:
            return False
    return True

# Example usage
print(is_palindrome_manual("A man a plan a canal Panama"))  # True
print(is_palindrome_manual("Hello"))  # False




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    count_vowels = sum(1 for char in s if char in vowels)
    count_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return count_vowels, count_consonants


def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list


def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
