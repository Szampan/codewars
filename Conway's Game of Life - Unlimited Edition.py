def neighbors_live(cells, row_number, col_number):
    neighbors = 0
    for i in range(max(row_number - 1, 0), min(row_number + 1, len(cells)-1)+1):
        for j in range(max(col_number - 1, 0), min(col_number + 1, len(cells[i])-1)+1):
            if (i, j) != (row_number, col_number):
                neighbors += cells[i][j]
    return neighbors


def will_live(live, live_neighbors):
    if live_neighbors == 3:
        return 1
    elif live_neighbors == 2 and live:
        return 1
    return 0


def add_margins(matrix):
    return [[0] * (len(matrix[0]) + 2)] + [[0] + row + [0] for row in matrix] + [[0] * (len(matrix[0]) + 2)]    


def trim(matrix):
    for row in (-1, 0):
        while not any(matrix[row]):
            matrix.pop(row)
    matrix = rotate(matrix, True)
    for row in (-1, 0):
        while not any(matrix[row]):
            matrix.pop(row)
    return(rotate(matrix, False))

# Different trimming solution:
# def trim(cells):
#   while not any(cells[0]): del cells[0]
#   while not any(cells[-1]): del cells[-1]
#   while not any([row[0] for row in cells]): map(lambda x: x.pop(0), cells)
#   while not any([row[-1] for row in cells]): map(lambda x: x.pop(), cells)

def rotate(matrix, cw = True):
    if cw:
        return list(map( list, list(zip(*matrix[::-1]))))
    return list(map(list, list(zip(*matrix))[::-1]))


def get_generation(cells, generations):
    gen = 0 
    while gen < generations:
        cells = add_margins(cells)
        gen += 1
        new_cells = [[0] * len(i) for i in cells]
        for row_num, row in enumerate(cells):
            for col_num, cell in enumerate(row):
                live_neighbors = neighbors_live(cells, row_num, col_num)
                new_cells[row_num][col_num] = will_live(cell, live_neighbors)
        cells = trim(new_cells)
    return cells


if __name__ == "__main__":
        
    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
             
    end   = [[0,1,0],
             [0,0,1],
             [1,1,1]]


    start1 = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]

    start2 = [[1, 0, 0], [0, 1, 1], [1, 1, 0]] 


    # resp = get_generation(start2, 5)




