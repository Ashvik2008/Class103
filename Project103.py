import pandas as pd
import plotly.express as px

df=pd.read_csv('/Users/vtai/Downloads/class103/Copy+of+data+-+data.csv')
fig=px.scatter(df,x="date",y="cases",title="Covid Cases in the World",color="country")
fig.show()