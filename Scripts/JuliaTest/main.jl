#using Pkg
#Pkg.add("CSV")
#Pkg.add("DataFrames")

using CSV
using DataFrames
# Import CSV files
# btc = CSV.read("../Data/BTC.csv", DataFrames)
csv_reader = CSV.File("../Data/NASDAQ.csv")
println(typeof(csv_reader))

for row in csv_reader
    println("values: $(row.Date), $(row.Open), $(row.Volume)")
end