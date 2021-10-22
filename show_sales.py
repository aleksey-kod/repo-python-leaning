import sys
if __name__ == "__main__":
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if len(sys.argv)==1:
           for line in f:
              print(line.split(" ")[1],end="")
        elif len(sys.argv)==2:
           for line in f:
              if line.split(" ")[0]>=sys.argv[1]:
                  print(line.split(" ")[1],end="")
        else:
           if len(sys.argv)==3:
              for line in f:
                 if (sys.argv[1]>= line.split(" ")[0] <= sys.argv[1]):
                    print(line.split(" ")[1], end="")
           


