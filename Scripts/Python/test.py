from coalas import csvReader as c 

def mean(dSet):
    µ = 0 
    for x in dSet:
        µ += x
    print(µ)
if __name__ == "__main__":
    c.importCSV(../../Data/BTC.csv)
    mean()
