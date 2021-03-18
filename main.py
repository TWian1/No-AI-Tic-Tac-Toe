xos = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
valnum = ["1", "2", "3"]
vallet = ["a", "b", "c"]
import random
def printboard(b):
    print("  1 2 3")
    print("a " + b[0] + " " + b[1] + " " + b[2])
    print("b " + b[3] + " " + b[4] + " " + b[5])
    print("c " + b[6] + " " + b[7] + " " + b[8])
def ait(b, c, d):
    if d == 1:
        if c == 0:
            while True:
                a = random.randint(0, 8)
                if b[a] == "_":
                    break
            return(a)
def checkwin(a, b):
  d = False
  if a[0] == b and a[1] == b and a[2] == b:
    d = True
  if a[0] == b and a[3] == b and a[6] == b:
    d = True
  if a[0] == b and a[4] == b and a[8] == b:
    d = True
  if a[1] == b and a[4] == b and a[7] == b:
    d = True
  if a[2] == b and a[5] == b and a[8] == b:
    d = True
  if a[3] == b and a[4] == b and a[5] == b:
    d = True
  if a[6] == b and a[6] == b and a[8] == b:
    d = True
  if a[6] == b and a[4] == b and a[2] == b:
    d = True
  return d
print("TIC TAC TOE!!! \n")
r = random.randint(0,1)
v = "o"
p = "x"
if r == 0:
    v = "x"
    p = "o"
    print("You are x's \n")
else:
    print("You are o's \n")
while True:
    printboard(xos)
    while True:
        x = input("\n qs (Letter Number): ")
        if len(x) == 2:
            if x[0] in vallet:
                if x[1] in valnum:
                    if x[0] == "a":
                        x = "1" + x[1]
                    elif x[0] == "b":
                        x = "2" + x[1]
                    else:
                        x = "3" + x[1]
                    a = int(x[0])
                    z = int(x[1])
                    z = z - 1
                    for i in range(a-1):
                        z = z + 3
                    if xos[z] == "_":
                        break
                else:
                  print("2 not num")
            else:
              print("1 not let")
        else:
          print("not 2 let")
    xos[z] = v
    m = checkwin(xos, v)
    if m == True:
      print("you won!")
      break
    h = ait(xos, 0, 1)
    xos[h] = p
    m = checkwin(xos, p)
    if m == True:
      print("You Lost. HOW")
      break