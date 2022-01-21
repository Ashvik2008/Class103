import pandas as pd
df=pd.DataFrame()
print(df)

import pandas as pd
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

import pandas as pd
data=[['S101','Amy',70],['S102','Bandhi',69],['S104','Cathy',75]]

df=pd.DataFrame(data,columns=['ID','Name','Marks'])
print(df)


#df=df.append(df2,ignore_index=True)
#print(df)