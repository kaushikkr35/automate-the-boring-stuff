table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):

    colWidths = [0] * len(table)


    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(colWidths[i][j]) > colWidths[i]:
                colWidths[i] = len(colWidths[i][j])


    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust[colWidths[y]], end = ' ')
        print(' ')

print_table(table_data)
    
