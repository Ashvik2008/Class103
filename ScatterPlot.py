from sys import implementation
import pandas as pd
import plotly.express as px

df=pd.read_csv("/Users/vtai/Downloads/class103/data.csv")
fig=px.scatter(df,x="Population",y="Per capita",title="Per Capita Income",size='Percentage',color="Country",size_max=75,)
fig.show()