from algorithm.matrix.matrix import display, rotate, transpose, select_cols, select_rows




mat = [[1,2,3],[4,5,6]]

display(mat)

display(transpose(mat))

display(rotate(mat))



mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
display(select_rows(mat, [0,2]))


display(select_cols(mat,[0,2,3]))