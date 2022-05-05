# from icecream import ic
import time
start_time = time.time()

def idx_of_last_not_one(lst):
    # print('IDX', lst)
    
    output = len(list(filter(lambda item: item > 1, lst)))-1
    # print('IDX', lst, output)
    return output

def completed_partition(lst, n):
    while sum(lst) != n:
        if n - sum(lst) >= min(lst):
            lst.append(min(lst))
        else:
            lst.append(n-sum(lst))
    return lst
    

def partitions(n):
    # print(n)
    tmp_partition = [n]
    noip = 1
    while max(tmp_partition) != 1: 
        tmp_num_idx = idx_of_last_not_one(tmp_partition)
        tmp_num = tmp_partition[tmp_num_idx]
        tmp_partition = tmp_partition[:tmp_num_idx] + [tmp_num-1]
        tmp_partition = completed_partition(tmp_partition, n)
            
        # tmp_partition = sorted(tmp_partition, reverse=True)
        tmp_partition.sort(reverse=True)
        noip += 1

    return noip

"""
while true:
    tmp_last = skopiuj tymczasowo ostatnią listę z listy
    tmp_num = last.pop() najmniejszy element (ale większy od 1)
    tmp_last.append(tmp_num-1)
    add_remaining_numbers() # nie większe od tmp_num
"""





print(partitions(5), "  ←- should equal 7")  
print(partitions(25), "  ←- should equal 1958")  
for _ in range(5):
    partitions(40)

print("--- %s seconds ---" % (time.time() - start_time))

#     '''define a function which returns the number of integer partitions of n'''
#     ones = [1] * n
    
#     print(ones, n)
# #     2. rekurencja: 
#         def shorten(partitions):
#             new_partitions = set()
#             for part in partitions:
#                 if part == [n]:
#                     pass
#                 else:
#                     pass
        
# #             przerwij jeśli len(lista)==1
# #             shorter_lists = [weź listę i na jej podstawie stwórz wszystkie możliwe listy o długości mniejszej o 1 ]:
# #                  set(spróbuj dodać każdą z liczb do każdej innej liczby)
# #             return set([lista] + shorten([shorter_lists]))
        
# #     3. return len(shorten(lista))
# # ALBO
# rekurencja
# dodawaj nowe następujące listy:
# dla każdej number w liście:
#     dla każdej liczby rzeczywistej i >= number/2:
#         zmniejsz number w liście o i
#         dodaj i na koniec listy ( do rozpatrzenia w następnym etapie rekurencji)
    