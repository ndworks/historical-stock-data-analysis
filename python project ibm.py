#!/usr/bin/env python
# coding: utf-8

# # ##Analyzing Historical Stock/Revenue Data and Building a Dashboard

# In[13]:


get_ipython().system('pip install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip install bs4')
#!pip install plotly


# In[14]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[15]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[16]:


Tesla = yf.Ticker('TSLA')


# In[17]:


tesla_data = Tesla.history(period = "max")


# In[18]:


tesla_data.reset_index(inplace = True)
tesla_data.head()


# In[7]:


#Question 2: Use Webscraping to Extract Tesla Revenue Data


# In[8]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[9]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[20]:


soup = BeautifulSoup(html_data,"html5lib")


# In[21]:


tesla_revenue= pd.read_html(url, match="Tesla Quarterly Revenue", flavor='bs4')[0]
tesla_revenue=tesla_revenue.rename(columns = {'Tesla Quarterly Revenue(Millions of US $)': 'Date', 'Tesla Quarterly Revenue(Millions of US $).1': 'Revenue'}, inplace = False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",","").str.replace("$","")
tesla_revenue.head()


# In[22]:


tesla_revenue


# In[23]:


tesla_revenue.dropna(inplace=True)
tesla_revenue.tail()


# In[24]:


#Question 3: Use yfinance to Extract Stock Data


# In[25]:


gamestop = yf.Ticker("GME")


# In[26]:


gme_data=gamestop.history(period="max")


# In[27]:


gme_data.reset_index(inplace=True)
gme_data.head()


# In[28]:


#Question 4: Use Webscraping to Extract GME Revenue Data


# In[29]:


url="https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data=requests.get(url).text


# In[30]:


soup = BeautifulSoup(html_data,"html5lib")


# In[36]:


gme_revenue= pd.read_html(url, match="GameStop Quarterly Revenue", flavor='bs4')[0]
gme_revenue=gme_revenue.rename(columns = {'GameStop Quarterly Revenue(Millions of US $)': 'Date', 'GameStop Quarterly Revenue(Millions of US $).1': 'Revenue'}, inplace = False)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",","").str.replace("$","")


# In[33]:


gme_revenue.dropna(inplace=True)
gme_revenue.tail()


# In[37]:


#Question 5: Plot Tesla Stock Graph


# In[38]:


make_graph(tesla_data, tesla_revenue, 'Tesla Stock Data Graph')


# In[39]:


make_graph(gme_data, gme_revenue, 'GameStop Stock Data Graph')


# In[ ]:





# # thankyou
# 
