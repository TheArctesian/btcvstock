from coalas import csvReader as c

def check(d1, d2):
    for i in range(len(d2)): 
        if list(d1)[i] == list(d2)[i]:
            print(list(d1)[i])
if __name__ == "__main__":
    c.importCSV("../../Data/c.csv")
    c.printHeaders()
    btdic = dict()
    nsdic = dict()
    for i in range(len(c.Timestamp)):
        btdic[c.Timestamp[i]] = c.Bprice[i] 

    for i in range(len(c.Date)):
        nsdic[c.Date[i]] = c.Open[i]

    check(btdic,nsdic)


