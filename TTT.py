def sum(a,b,c):
    return a + b + c

def printGame(xA, xZ):
    
    z = 'X' if xA[0] else ('O' if xZ[0] else 0)
    o = 'X' if xA[1] else ('O' if xZ[1] else 1)
    t = 'X' if xA[2] else ('O' if xZ[2] else 2)
    th = 'X' if xA[3] else ('O' if xZ[3] else 3)
    f = 'X' if xA[4] else ('O' if xZ[4] else 4)
    fi = 'X' if xA[5] else ('O' if xZ[5] else 5)
    s = 'X' if xA[6] else ('O' if xZ[6] else 6)
    se = 'X' if xA[7] else ('O' if xZ[7] else 7)
    e = 'X' if xA[8] else ('O' if xZ[8] else 8)

    print(f"{z} | {o} | {t} ")
    print(f"--|---|---")
    print(f"{th} | {f} | {fi} ")
    print(f"--|---|---")
    print(f"{s} | {se} | {e} ")

def CWin(xA, xZ):
    won = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for win in won:
      if (sum(xA[win[0]], xA[win[1]], xA[win[2]]) == 3):
          print("\nX won the game")
          return 1
      if (sum(xZ[win[0]], xZ[win[1]], xZ[win[2]]) == 3):
          print("\nO won the game")
          return 0
    return -1

if __name__ == "__main__":
    xA = [0, 0, 0, 0, 0, 0,0, 0, 0]
    xZ = [0, 0, 0, 0, 0, 0,0, 0, 0]
    turn = 1
    print("Tic Tac Toe")
    while(True):
        printGame(xA, xZ)
        if(turn == 1):
           print("\nX turn\n")
           value = int(input("\nPlease enter a value: "))
           xA[value] = 1
        else:
           print("\nO turn\n")
           value = int(input("Please enter a value: "))
           xZ[value] = 1
        Gwin = CWin(xA, xZ)
        if(Gwin != -1):
          print("\nGame Over")
          break

        turn = 1 - turn
