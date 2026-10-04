# Unit II Case Study
# Sparse Matrix / 2D Triplet Representation
#
# Each row stores:
# [row, column, value]

sparse_connections = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 3, 1],
    [2, 4, 1],
    [3, 1, 1],
    [4, 2, 1]
]

print("Existing connections:")

for row, column, value in sparse_connections:
    print(f"User {row} -> User {column} = {value}")
