from coalas import csvReader as c

c.importCSV("../../Data/c.csv")
c.printHeaders()
c.writeCSV("data.csv")
