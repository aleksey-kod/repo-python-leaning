import sys
if __name__ == "__main__":
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        for line in f:
            pass
        dataraw = str(line).split()
        idx=int(dataraw[0])+1
        data = '\n'+str(idx)+' '+(sys.argv[1])
        f.writelines(data)

