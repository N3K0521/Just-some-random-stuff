def determinant(M):
    # Base case of recursive function: 2x2 matrix (such that det(M) = ad - cb)
    if len(M) == 2:
        return (M[0][0] * M[1][1]) - (M[0][1] * M[1][0])
    else:
        total = 0
        for column, element in enumerate(M[0]):
            # Exclude first row and current column.
            K = [x[:column] + x[column + 1 :] for x in M[1:]]
            # Given that the element is in row 1, sign is negative if index is odd.
            if column % 2 == 0:
                total += element * determinant(K)
            else:
                total -= element * determinant(K)
        return total