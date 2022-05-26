def encode(s):
    if s == '':
        return ('', None)
    matrix = sorted([s[i:] + s[:i] for i in reversed(range(len(s)))])

    ind = matrix.index(s)
    last_col = ''.join([i[-1] for i in matrix])    
    return (last_col, ind)

def decode(last_col, n):     
    if last_col == '':
        return ''
    first_col = ''.join(sorted(last_col))    
    t = []
    for letter in first_col:
        indexes = [i for i, n in enumerate(last_col) if n == letter ]
        for i in indexes: 
            if i not in t:
                t.append(i)
                break
    decoded = ''
    i = t[n]
    for _ in range(len(last_col)):
        decoded += (last_col[i])
        i = t[i]

    return decoded
