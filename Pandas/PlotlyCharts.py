from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode, plot, iplot
import pandas as pd
import matplotlib.pyplot as plt

init_notebook_mode(connected=True)

cf.go_offline()
df = pd.read_csv('../Datasets/datasets_19_420_Iris.csv')
print(df.columns)
# df['SepalWidthCm'].plot(kind='hist')
# df['SepalWidthCm'].plot(kind='hist')
df.iplot()
plt.show()
