import pandas as pd
import plotly.express as px

df=pd.read_csv("/Users/vtai/Downloads/class103/line_chart.csv")
fig=px.line(df,x="Year",y="Per capita income", color='Country',title="Per capita income")
fig.show()