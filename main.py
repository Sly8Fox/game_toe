
"""
meta_map = [[-1, 0, 1],
            [0, 1, 1],
            [0, 0, -1]]
-1 - пусто
0 - нолик
1 - крестик
"""
dict_toe = {
    0: "0",
    1: "X",
    -1: " "
}

# ┼│─
def fill_map(meta_map):
    print("  1 2 3")
    for i in range(0, 3):
        print(i+1, end=" ")
        for j in range(0, 3):
            print(dict_toe[meta_map[i][j]], end="")
            if j != 2:
                print("│", end="")
        if i != 2:
            print("\n  ─┼─┼─")

meta_map = [[-1, 0, 1],
            [0, 1, 1],
            [0, 0, -1]]


fill_map(meta_map)
