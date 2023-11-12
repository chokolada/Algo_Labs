def zalivka(start_node, changing_color, color_to_switch):
    with open("input.txt", "r") as file:
        matrix = [list(map(str, line.strip().split())) for line in file]

    rows = start_node[0]
    columns = start_node[1]

    matrix = [matrix[i][:columns] for i in range(rows)]
    row, column = changing_color
    searched_color = matrix[row][column]

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    neighbor_map = {}
    visited = set()
    neighbor_to_bfs = []

    def loop(node):
        neighbor_map[node] = []
        visited.add(node)

        for dr, dc in directions:
            neighbor_row, neighbor_column = node[0] + dr, node[1] + dc
            neighbor = (neighbor_row, neighbor_column)

            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_column < columns
                and matrix[neighbor_row][neighbor_column] == searched_color
            ):
                neighbor_map[node].append(neighbor)
                neighbor_to_bfs.append(neighbor)

    def bfs(neighbor_map):
        for neighbor in neighbor_map:
            if neighbor not in visited:
                loop(neighbor)
    neighbor_to_bfs.clear()

    loop(changing_color)
    bfs(neighbor_to_bfs)

    for node, neighbors in neighbor_map.items():
        print(f"{node}: {neighbors}")

    for node in neighbor_map:
        matrix[node[0]][node[1]] = color_to_switch

    for row in matrix:
        print(" ".join(row))

# Example usage
zalivka((10, 10), (9, 9), "'B',")
