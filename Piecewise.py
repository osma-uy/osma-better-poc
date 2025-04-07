import piecewise_regression
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # or "TkAgg", "Agg", etc.

file_path = 'PieceWise_Frio.xlsx'
df = pd.read_excel(file_path)

x = df['T ext promedio'].tolist()
y = df['kWh Promedio por dia'].tolist()

pw_fit = piecewise_regression.Fit(x, y, n_breakpoints=1, start_values=None)
print(pw_fit.summary())

# Plot the data, fit, breakpoints and confidence intervals
pw_fit.plot_data(color="grey", s=20)
# Pass in standard matplotlib keywords to control any of the plots
pw_fit.plot_fit(color="red", linewidth=4)
pw_fit.plot_breakpoints()
pw_fit.plot_breakpoint_confidence_intervals()
plt.xlabel("Text Promedio")
plt.ylabel("kWh por dia")
plt.show()
plt.close()