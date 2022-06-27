
using DataFrames, CSV
using Cairo, Gadfly

data = CSV.read("simulate_public.csv")
p = plot(data, x=:p, y=:Expected, Geom.point);
img = SVG("public_plot.svg", 6inch, 4inch)
draw(img, p)data = CSV.read("simulate_public.csv")
