import pandas as pd
import time
from chat.vector_store import Chroma


db = Chroma()
# add embeddings for brands
# df = pd.read_excel('C:/Users/caijq/Downloads/机场项目数据整理/embedding/brand.xlsx')
# brand_collection = db.get_or_create_collection(name='brand')
# n = 0
# while n <= df.shape[0]:
#     db.add(name='brand',
#         documents=list(df.loc[n:n+1999, 'brand_name']),
#         ids=list(df.loc[n:n+1999, 'id'].astype(str)),
#         metadatas=df.loc[n:n+1999, :].to_dict(orient='records'))
#     n += 2000
#     time.sleep(20.0)
# add embeddings for malls
df = pd.read_excel('C:/Users/caijq/Downloads/机场项目数据整理/embedding/mall_name-with-city.xlsx')
mall_shape = df.shape[0]
db.get_or_create_collection(name='mall_name-with-city')
n = 0
while n <= df.shape[0]:
    db.add(name='mall_name-with-city',
        documents=list(df.loc[n:n+1999, 'mall_name']),
        ids=list(df.loc[n:n+1999, 'id'].astype(str)),
        metadatas=df.loc[n:n+1999, :].to_dict(orient='records'))
    n += 2000
    time.sleep(20.0)
