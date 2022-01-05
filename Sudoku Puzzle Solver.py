puzzle = [[0,0,7,0,3,0,2,0,5],
          [3,0,0,5,6,2,8,0,4],
          [0,2,0,0,8,4,1,0,3],
          [4,0,8,2,0,0,0,1,0],
          [0,0,0,0,5,0,0,2,7],
          [9,7,2,1,0,0,3,0,8],
          [0,0,1,4,0,0,5,3,6],
          [0,0,4,0,0,5,0,8,0],
          [6,8,0,0,0,0,0,0,0]          
         ]

row = [[],[],[],[],[],[],[],[],[]]
col = [[],[],[],[],[],[],[],[],[]]
sqr = [[],[],[],[],[],[],[],[],[]]

choices = []

# puzzle[row 0-8][col 0-8]

for i in puzzle:
  print(i)

class Sudoku:
  def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')

  def update():
    #Creates a list for all the rows
    for m in range(9):
      row[m].append(puzzle[m])

    #Creates a list for all the columns
    for n in range(9):
      for o in range(9):
        col[n].append(puzzle[o][n])

    #Creates a list for all the subsquares
    for i in range(3):
      for j in range(3):
        sqr[0].append(puzzle[i][j])
    for i in range(3):
      for j in range(3,6):
        sqr[1].append(puzzle[i][j])
    for i in range(3):
      for j in range(6,9):
        sqr[2].append(puzzle[i][j])
    for i in range(3,6):
      for j in range(3):
        sqr[3].append(puzzle[i][j])
    for i in range(3,6):
      for j in range(3,6):
        sqr[4].append(puzzle[i][j])
    for i in range(3,6):
      for j in range(6,9):
        sqr[5].append(puzzle[i][j])
    for i in range(6,9):
      for j in range(3):
        sqr[6].append(puzzle[i][j])
    for i in range(6,9):
      for j in range(3,6):
        sqr[7].append(puzzle[i][j])
    for i in range(6,9):
      for j in range(6,9):
        sqr[8].append(puzzle[i][j])

  update()

  def possible(puzzle, x, y, z):
    if puzzle[x][y] == 0:
   
      #Finds all the possible choices given a certain row, col, and subsquare
      a = list(row[x])
      b = list(col[y])
      c = list(sqr[z])
    
      used = []
    
      #Used in Rows
      for j in a[0]:
        if j not in used:
          used.append(j)
    
      #Used in Cols
      for j in b:
        if j not in used:
          used.append(j)
    
      #Used in Subsquare
      for j in c:
        if j not in used:
          used.append(j)
    
      #Find the remaining choice
      used.remove(0)
    
      choices = []
      for i in range(1,10):
        if i not in used:
          choices.append(i)
    
    else:
      choices = []
    
    return choices
    

  def solve(puzzle):
    for i in puzzle:
      for j in i:
        if j == 0:
          #1st Subsquare
          for i in range(3):
            for j in range(3):
              if len(Sudoku.possible(puzzle, i, j, 0)) == 1:
                result = Sudoku.possible(puzzle, i, j, 0)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)

          
          #2nd Subsquare
          for i in range(3):
            for j in range(3,6):
              if len(Sudoku.possible(puzzle, i, j, 1)) == 1:
                result = Sudoku.possible(puzzle, i, j, 1)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)
          
          #3rd Subsquare
          for i in range(3):
            for j in range(6,9):
              if len(Sudoku.possible(puzzle, i, j, 2)) == 1:
                result = Sudoku.possible(puzzle, i, j, 2)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)

          #4th Subsquare
          for i in range(3,6):
            for j in range(3):
              if len(Sudoku.possible(puzzle, i, j, 3)) == 1:
                result = Sudoku.possible(puzzle, i, j, 3)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)

          #5th Subsquare
          for i in range(3,6):
            for j in range(3,6):
              if len(Sudoku.possible(puzzle, i, j, 4)) == 1:
                result = Sudoku.possible(puzzle, i, j, 4)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)

          #6th Subsquare
          for i in range(3,6):
            for j in range(6,9):
              if len(Sudoku.possible(puzzle, i, j, 5)) == 1:
                result = Sudoku.possible(puzzle, i, j, 5)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)
          
          #7th Subsquare
          for i in range(6,9):
            for j in range(3):
              if len(Sudoku.possible(puzzle, i, j, 6)) == 1:
                result = Sudoku.possible(puzzle, i, j, 6)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)
          
          #8th Subsquare
          for i in range(6,9):
            for j in range(3,6):
              if len(Sudoku.possible(puzzle, i, j, 7)) == 1:
                result = Sudoku.possible(puzzle, i, j, 7)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)
          
          #9th Subsquare
          for i in range(6,9):
            for j in range(6,9):
              if len(Sudoku.possible(puzzle, i, j, 8)) == 1:
                result = Sudoku.possible(puzzle, i, j, 8)
                result1= Sudoku.listToStringWithoutBrackets(result)
                puzzle[i][j] = int(result1)
                Sudoku.update()
                Sudoku.solve(puzzle)
        else:
          break

print("-------")

Sudoku.solve(puzzle)

for i in puzzle:
  print(i)
