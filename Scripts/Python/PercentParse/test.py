from coalas import csvReader as c 

def mean(Set):
    sum = 0 
    for x in Set:
        sum += x
# Sum of price / length  
    µ = sum/len(Set)  
    print(µ)
    return(µ)

def norm(Set, NewSet):
    for x in range(len(Set)):
        if x != len(Set):
            pi = percInc(Set[x+1], Set[x]) 
            Newset.append(pi)

# x == New Value
# y == Original Value
# Inc == Increase 
# Pi == Percent Increase

def percInc(x,y):
    incr = x - y 
    pi = incr/y*100
    return(pi)

if __name__ == "__main__":
    c.importCSV('t.csv')
    c.addCol("BtcPer")
    c.addCol("NasPer")
    print(type(c.Bprice[1]))
    for i in range(len(c.Bprice)):
        c.Bprice[i] = int(c.Bprice[i])
        c.Open[i] = int(c.Open[i])
    print(type(c.Bprice[1]))

    for i in range(len(c.Bprice)):
        if i != len(c.Bprice):
            try: 
                c.BtcPer.append(percInc(c.Bprice[i+1],c.Bprice[i]))
            except IndexError: 
                print(f'index at {i}')

    for i in range(len(c.Open)):
        if i != len(c.Open):
            try: 
                c.NasPer.append(percInc(c.Open[i+1],c.Open[i]))
            except IndexError: 
                print(f'index at {i}')


    print(c.NasPer)
    c.printHeaders()
    c.writeCSV("percent.csv")
    mean(c.Bprice)
