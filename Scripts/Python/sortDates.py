from coalas import csvReader as c

def check(d1, d2): # btcD, nsD
    for i in range(len(d2)): 
        if list(d1).contains(list(d2)[i]):
            print("")
        else: 
            print("not")
if __name__ == "__main__":
    c.importCSV("data.csv")
    c.printHeaders()
    btdic = dict()
    nsdic = dict()
    t = []
    for i in c.Timestamp:
        t.append(i)
    for i in range(len(c.Timestamp)):
        btdic[c.Timestamp[i]] = c.Bprice[i] 

    for i in range(len(c.Date)):
        nsdic[c.Date[i]] = c.Open[i]

    for i in range(len(t)):
        if t[i] in c.Date:
            print(f'{c.col.PASS}yes{c.col.ENDC}')
        else:
            print(f'{c.col.FAIL}no{c.col.ENDC}')
            ind = c.Timestamp.index(t[i])
            c.Timestamp.pop(ind)
            c.Bprice.pop(ind)

    print(len(c.Timestamp))
    for x in c.Date:
        if x == "":
            c.Date.remove('')
    print(len(c.Date))
