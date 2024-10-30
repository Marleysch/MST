import copy

from sqlalchemy.dialects.mysql.base import MSTinyText


def create_matrix(file):
    with open(file, 'r') as file:
        content = file.read()
    content = content.replace(" ", "")
    content = content.replace("{", "")

    matrix = []
    row = []
    num = ''
    i = 0
    stop = len(content)
    while i != stop:
        if content[i] == '}':
            num = float(num)
            row.append(num)
            num = ''
            matrix.append(row)
            row = []
            i += 2
        elif content[i] == ',':
            num = float(num)
            row.append(num)
            num = ''
            i += 1
        else:
            num += content[i]
            i += 1

    for i in range(len(matrix)):
        matrix[i][0] = int(matrix[i][0])
        matrix[i][1] = int(matrix[i][1])
    return matrix

def creates_cycle(v1, v2, adj):
    v1 -= 1
    v2 -= 1
    if v1 < v2:
        temp = v1
        v1=v2
        v2 = temp
    # print(v1,v2)
    done = [v2]

    todo = copy.deepcopy(adj[v2])
    # print(todo)
    while todo:
        for i in range(len(adj[todo[0]])):
            if adj[todo[0]][i] == v1:
                return True
            if adj[todo[0]][i] not in todo and adj[todo[0]][i] not in done:
                todo.append(adj[todo[0]][i])

        # print(todo)
        done.append(todo[0])
        todo.pop(0)
    return False

def create_MST(edge_list):
    MST = []
    sorted_el = sorted(edge_list, key=lambda x: x[2])

    order = 0
    for edge in sorted_el:
        if edge[0] > order:
            order = edge[0]
        if edge[1] > order:
            order = edge[1]

    # print(f'sortedel: {sorted_el}')

    MST_adjacency = [[] for _ in range(order)]
    while sorted_el:
        edge = sorted_el[0]
        # print(creates_cycle(edge[1], edge[0], MST_adjacency))
        if not creates_cycle(edge[1], edge[0], MST_adjacency):
            MST.append(edge)
            MST_adjacency[edge[0]-1].append(edge[1]-1)
            MST_adjacency[edge[1]-1].append(edge[0]-1)
        sorted_el.pop(0)
    return MST

def main():

    for i in range(1,11):
        edge_list = create_matrix(f"{i}.txt")
        MST = create_MST(edge_list)
        MST_weight = 0
        for i in range(len(MST)):
            MST_weight +=MST[i][2]
        print(f'Weight: {MST_weight}')

if __name__ == "__main__":
    main()