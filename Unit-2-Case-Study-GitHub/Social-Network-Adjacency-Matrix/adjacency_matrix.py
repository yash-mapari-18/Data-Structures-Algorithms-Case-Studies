# Unit II Case Study
# Social Network Adjacency Matrix

users = ["U1", "U2", "U3", "U4", "U5"]

connections = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]


def check_connection(user1, user2):
    return connections[user1][user2] == 1


print("Social Network Connections:")

for i in range(len(users)):
    print(users[i], ":", connections[i])

print("\nChecking U1 and U2:")

if check_connection(0, 1):
    print("U1 and U2 are friends.")
else:
    print("U1 and U2 are not friends.")
