from coalas import csvReader as c

def netDif(btc,nas):
    btc = float(btc)
    nas = float(nas)
    dif = 0
    if btc > nas: 
        dif = btc-nas 

    if nas > btc: 
        dif = nas-btc 
    return dif

def dif(a,b):
    a = float(a)
    b = float(b)
    return a - b

if __name__ == "__main__":
    c.importCSV("../PercentParse/percent.csv")
    c.addCol("dif")
    c.addCol("netDif")

    for i in range(len(c.BtcPer)):
        d = dif(c.BtcPer[i],c.NasPer[i])
        nd = netDif(c.BtcPer[i],c.NasPer[i])
        c.dif.append(d)
        c.netDif.append(nd)

    c.writeCSV("dif.csv")
    df = 0.0
    ndf = 0.0
    for v in c.dif:
        df += v

    for v in c.netDif:
        ndf += v

    print(f'Avg Dif = {df/len(c.dif)}')
    print(f'Avg Net Dif = {ndf/len(c.netDif)}')
