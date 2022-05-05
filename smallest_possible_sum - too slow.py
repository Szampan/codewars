from icecream import ic
import time
start_time = time.time()

def solution1(a):   #  much faster
    a_len = len(a)
    a = set(a)
    while len(a) != 1:
        b = max(a)
        a.remove(b)
        a.add(b-max(a))
    return(max(a) * a_len)

def solution(a):
    # print(a)
    def almost_max(lst):
        # if len(set(lst)) == 1:
        #     return
        # else:
        #     lst = sorted(list(set(lst)))
        #     return lst[-2]

        try: 
            return sorted(list(set(lst)))[-2]
        except:
            return

        # lst = sorted(list(set(lst)))
        # if len(lst) > 1:
        #     return lst[-2]
        # return

    """
    def transform_rec(lst):
        lst[lst.index(max(lst))] = max(lst) - almost_max(lst)
        if almost_max(lst):
            lst = transform_rec(lst)
        return lst
    
    if almost_max(a):
        a = transform_rec(a)
    """ 
    """
    while True:
        if almost_max(a):
            a[a.index(max(a))] = max(a) - almost_max(a)
        if not almost_max(a):
            break
    """   
    def transform(lst):
        # print(lst)
        lst[lst.index(max(lst))] = max(lst) - almost_max(lst)
        return lst

    while True:
        if almost_max(a):
            a = transform(a)
        else:
            break

    return sum(a)   # smallest possible sum of all numbers in Array



if __name__ == "__main__":
    for _ in range(50):
        print(solution([9]))
        print(solution([6, 9, 21]))
        print(solution([1, 21, 55]))
    # print(solution([8486482500, 3099571425, 5490545625, 4581898425, 29662582500, 5431348800, 18327593700, 20675734425, 28030097700, 26574240825, 2310120000, 1186503300, 3011016825, 38360986425, 13584949425, 1299442500, 8412847425, 417265425, 11868883200, 32054358825, 9240480000, 3804639300, 17049327300, 4314790800, 14055796800, 25539820425, 10431635625, 12309249825, 11351031300, 14150928825, 24903735300, 16736979825, 26183926800, 33504600825]))
        print(solution(2*[193600, 176400, 40804, 119025, 166464, 42849, 136161, 111556, 179776, 7056, 53361, 9025, 193600, 47089, 183184, 139129, 24649, 120409, 160801, 32761, 88804, 223729, 150544, 10000, 186624, 235225, 198916, 30276, 46656, 74529, 37249, 61009, 94249, 48841, 239121, 55696, 198916, 213444, 55225, 167281, 8100, 50176, 16384, 15129, 79524, 81225, 246016, 48841, 14884, 131769, 13924, 2500, 2601, 12321, 146689, 75625, 195364, 113569, 12544, 209764, 126736, 130321, 57121, 247009, 84100, 179776, 3364, 21609, 88804, 14884, 3249, 157609, 78400, 7921, 147456, 21316, 90601, 209764, 119716, 8464, 7396, 99856, 248004]))
        print(solution([37249, 213444, 42025, 124609, 6724, 139129, 11449, 144400, 63504, 5929, 2916, 131044, 174724, 8281, 130321, 65536, 237169, 7225, 138384, 218089, 75076, 40804, 225625, 28900, 61009, 213444]))

    print("--- %s seconds ---" % (time.time() - start_time))