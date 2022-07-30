from coalas import csvReader as c

c.importCSV("./t.csv")
c.printHeaders()

for i in range(len(c.Timestamp)):
    if c.Timestamp[i] != c.Date[i]:
        print(f'{c.col.FAIL}Not the same at: {i}{c.col.ENDC}')


# Yay it all works
