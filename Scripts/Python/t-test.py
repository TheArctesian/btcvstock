from coalas import csvReader as c 

def percentIncrease(i1, i2):
    increase = i2 - i1
    perInc = increase/i2*100
    return perInc
if __name__ == "__main__":
    c.importCSV('t.csv')
    c.addCol("BtcPer")
    c.addCol("NasPer")
    c.printHeaders()
    for i in range(len(c.Bprice)):
        c.Bprice[i] = int(c.Bprice[i])
        c.Open[i] = int(c.Open[i])
    for i in range(len(c.Bprice)):
        try: 
            Bper = percentIncrease(int(c.Bprice[i-1]), int(c.Bprice[i]))
            Nper = percentIncrease(int(c.Open[i-1]), int(c.Open[i]))
            print(Bper)
            #c.BtcPer[i] = Bper
            #c.NasPer[i] = Nper
            c.BtcPer.append(Bper)
            c.NasPer.append(Nper)
        except IndexError: 
            continue
            #c.BtcPer[i] = 0

            #c.NasPer[i] = 0
    print(c.BtcPer)
    c.writeCSV("s.csv")
