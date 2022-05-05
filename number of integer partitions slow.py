def idx_of_last_not_one(lst):
    # print('IDX', lst)
    output = len(list(filter(lambda item: item > 1, lst)))-1
    # print('IDX', lst, output)
    return output
    
    lst.index(min(filter(lambda item: item > 1, lst)))

def completed_partition(lst, n):
    new_lst = lst
    while sum(new_lst) != n:
        if n - sum(new_lst) >= min(new_lst):
            new_lst.append(min(new_lst))
        else:
            new_lst.append(n-sum(new_lst))
    return new_lst

def partitions(n):
    tmp_partition = [n]
    k = n
    noip = 1
    # while [1]*n not in partitions:
    while tmp_partition != [1]*n: 
        # tmp_partition = copy.deepcopy(partitions)[-1]
        # tmp_partition = tmp_partition[-1]
        tmp_num_idx = idx_of_last_not_one(tmp_partition)
        tmp_num = tmp_partition[tmp_num_idx]
        tmp_partition = tmp_partition[:tmp_num_idx]

        tmp_partition.append(tmp_num-1)

        
        # ic(tmp_num, tmp_partition)

        # ic(sum(tmp_partition), n-sum(tmp_partition))
        if sum(tmp_partition) < n:
            # ic(n - sum(tmp_partition))
            tmp_partition = completed_partition(tmp_partition, n)
        # partitions.append(sorted(tmp_partition, reverse=True))
        tmp_partition = sorted(tmp_partition, reverse=True)
        noip += 1
        k -= 1

    # print(partitions)
    # return len(partitions)
    return noip