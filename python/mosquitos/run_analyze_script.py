import analyze_mosquitos
import sys

# filename = "A2_mosquito_data.csv"
filename = sys.argv[1]
analyze_mosquitos.create_mosquitos_vs_tempC_plot(filename)
