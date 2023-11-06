# # find the second largest and second smallest


# l=[5,6,1,2,9,23,56,56,1]

# largest=second_largest=float('-inf')  # l[0]
# smallest=second_smallest=float('inf')  #l[0]


# for i in l:
#     if i > largest:
#         second_largest=largest
#         largest=i
#     elif i > second_largest and i!= largest:
#         second_largest=i
#     if i < smallest:
#         second_smallest=smallest
#         smallest=i
#     elif i < second_smallest and i !=smallest:
#         second_smallest=i
# print(largest)
# print(second_largest)
# print(smallest)
# print(second_smallest)


# # sorting list without using built-ins
# a = [5,6,1,2,9,23,56,56,1]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# find duplicates
# dup = [5,6,1,2,9,23,56,56,1]

# def find_duplicates(a):
#     unique_list=[]
#     duplicates_list=[]
#     for i in a:
#         if i not in unique_list:
#             unique_list.append(i)
#         else:
#             duplicates_list.append(i)
#     return f'duplicate are :{duplicates_list} unique are {unique_list}'

# print(find_duplicates(dup))

def find_duplicates(elements):
    duplicates,seen=set(),set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

print(find_duplicates([5,6,1,2,9,23,56,56,1]))

