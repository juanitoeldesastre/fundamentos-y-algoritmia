# matrices A y B
A <- matrix(c(2, 3, 1, 2, 0, 7), nrow = 3, byrow = TRUE)
B <- matrix(c(4, 9, 0, 6, 2, 7, 9, 2), nrow = 2, byrow = TRUE)

# multiplication
C <- A %*% B

# :cs
print(C)
