def server_finder(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        nodes, connections = map(int, lines[0].split())
        clients = list(map(int, lines[1].split()))
        connection_details = [list(map(int, line.split())) for line in lines[2:]]

    print("Nodes:", nodes)
    print("Clients:", clients)
    print("Connection Details:", connection_details)

    n = nodes

    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            for connection in connection_details:
                if connection[0] == i + 1 and connection[1] == j + 1:
                    dist[j][i] = connection[2]
                    dist[i][j] = connection[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    servers = []
    index_of_min = []
    ping_sum = [[],[],[]]
    min_ping = float('inf')

    for client in clients:
        servers.append(dist[client - 1])


    for server in servers:
        filtered_server = [value for value in server if value > 0]
        if filtered_server:
            index_of_min.append(server.index(min(filtered_server)))

    for i in range(len(servers)):
        index = index_of_min[i]
        for ping in servers:
            ping_sum[i].append(ping[index])



    sums = [sum(inner_list) for inner_list in ping_sum]
    print("Asfgas", sums)
    for ping in sums:
        if ping < min_ping:
            min_ping = ping

    print("Ping Sum:", ping_sum)

    return min_ping

result = server_finder("gamsrv.in")
with open("gamsrv.out", "w") as file:
    file.write(str(result))
print(result)
