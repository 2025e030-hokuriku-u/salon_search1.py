#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.version)


# In[2]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[3]:


#merged11.csvの読み込み
merged_df = pd.read_csv("merged.csv")


# In[4]:


st.title("飲食店サーチ")
price_limit = st.slider("ディナー平均", min_value=1000,    max_value=20000, step=200, value=5000)
score_limit = st.slider("星の下限", min_value=0.0,     max_value=5.0, step=1.0, value=5.0)


# In[5]:


filtered_df = merged_df[
    (merged_df['price'] <= price_limit)&
    (merged_df['star'] >= score_limit)
    ]


# In[6]:


fig = px.scatter(
    filtered_df,
    x='star',
    y='price',
    hover_data=['store_food','star'],        title='星数と食事平均価格の散布図'
)
st.plotly_chart(fig)


# In[7]:


selected_food = st.selectbox('気になる飲食店を選んで詳細を確認', filtered_df['store_food'])

if selected_food:
    url = filtered_df[filtered_df['store_food'] == selected_food]['link_food'].values[0]
    st.markdown(f"[{selected_food}のページへ移動]({url})", unsafe_allow_html=True)


# In[8]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("star", "review", "price")
)
ascending = True if sort_key == "price"else False


# In[9]:


st.subheader(f"{sort_key}による飲食店ランキング(上位10件)")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
st.dataframe(ranking_df[["store_food", "price", "star","review"]])


# In[ ]:




