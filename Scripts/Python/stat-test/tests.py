import researchpy as rp
import scipy.stats as stats
from coalas import csvReader as c
import pandas as pd

if __name__ == "__main__":

    # c.importCSV('../PercentParse/percent.csv')
    #c.printHeaders()
    
    df = pd.read_csv("../PercentParse/percent.csv")
    des, res = rp.ttest(df['BtcPer'], df['NasPer'])
    print(res)
    print(des)

