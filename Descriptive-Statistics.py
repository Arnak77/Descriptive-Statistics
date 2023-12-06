#!/usr/bin/env python
# coding: utf-8

# # Import necessary packages

# In[57]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load the file

# In[58]:


income_df=pd.read_csv(r"D:\NIT\4DEC\4th, 5th-Inferential stats\Descriptive stats _PRACTICLE/Inc_Exp_Data.csv")


# In[59]:


income_df


# In[4]:


income_df.head()


# In[5]:


income_df["Highest_Qualified_Member"].head()


# # Analyze the data

# In[6]:


income_df.info()


# In[7]:


income_df["Highest_Qualified_Member"]=income_df["Highest_Qualified_Member"].astype("category")


# In[8]:


income_df.info()


# In[9]:


income_df.shape


# In[10]:


income_df.describe()


# In[11]:


income_df.describe().T


# In[12]:


income_df.isna()


# In[13]:


income_df.isna().sum()


# In[14]:


income_df.isna().any()


# In[15]:


income_df.columns


# # What is the Mean Expense of a Household? and What is the Median Household Expense?

# In[16]:


income_df["Mthly_HH_Expense"].mean()


# In[17]:


income_df["Mthly_HH_Expense"].median()


# In[18]:


income_df["Mthly_HH_Income"].mean()


# In[19]:


income_df["Emi_or_Rent_Amt"].mean()


# In[20]:


income_df["Annual_HH_Income"].mean()


# In[21]:


income_df["No_of_Earning_Members"].mean()


# In[22]:


income_df["Mthly_HH_Income"].median()


# In[23]:


income_df["Annual_HH_Income"].median()


# In[24]:


income_df["Mthly_HH_Expense"].value_counts()


# # What is the Monthly Expense for most of the Households?

# In[25]:


income_df["Mthly_HH_Expense"].value_counts().max()


# In[26]:


income_df["Mthly_HH_Expense"].value_counts().min()


# In[27]:


mth_exp_tmp = pd.crosstab(index=income_df["Mthly_HH_Expense"], columns="count")
mth_exp_tmp.reset_index(inplace=False)
mth_exp_tmp[mth_exp_tmp['count'] == income_df.Mthly_HH_Expense.value_counts().max()]


# In[28]:


mth_exp_tmp = pd.crosstab(index=income_df["Mthly_HH_Expense"], columns="count")
mth_exp_tmp.reset_index(inplace=True)
mth_exp_tmp[mth_exp_tmp['count'] == income_df.Mthly_HH_Expense.value_counts().max()]


# In[29]:


mth_exp_tmp = pd.crosstab(index=income_df["Highest_Qualified_Member"], columns="count")
mth_exp_tmp.reset_index(inplace=True)
mth_exp_tmp[mth_exp_tmp['count'] == income_df.Highest_Qualified_Member.value_counts().max()]


# In[30]:


income_df["Highest_Qualified_Member"].value_counts()


# # Plot the Histogram to count the Highest qualified member

# In[31]:


# the type of plot to create. It can be 'line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie', etc. The choice of 'kind' determines the type of plot.


# In[32]:


income_df["Highest_Qualified_Member"].value_counts().plot(kind="line")


# In[33]:


income_df["Mthly_HH_Income"].value_counts().plot(kind="bar")


# In[34]:


income_df["No_of_Fly_Members"].value_counts().plot(kind="barh")


# In[35]:


income_df["Emi_or_Rent_Amt"].value_counts().plot(kind="hist")


# In[36]:


income_df["Annual_HH_Income"].value_counts().plot(kind="density")


# In[37]:


income_df["No_of_Earning_Members"].value_counts().plot(kind="area")


# In[ ]:





# In[38]:


income_df.columns


# In[39]:


income_df.plot(x="Mthly_HH_Income", y="Mthly_HH_Expense")


# # Calculate IQR(difference between 75% and 25% quartile)

# In[40]:


IQR=income_df["Mthly_HH_Expense"].quantile(0.75)


# In[41]:


IQR


# In[42]:


income_df["Mthly_HH_Expense"].quantile(0.25)


# In[43]:


income_df.plot(x="Mthly_HH_Income", y="Mthly_HH_Expense")
IQR=income_df["Mthly_HH_Expense"].quantile(0.75)-income_df["Mthly_HH_Expense"].quantile(0.25)
print("IQR",IQR)


# # Calculate Standard Deviation for first 4 columns.

# In[44]:


income_df.iloc[2]


# In[45]:


income_df.head()


# In[46]:


t=(income_df.iloc[:,0:5].std().to_frame())


# In[47]:


t


# In[48]:


pd.DataFrame(income_df.iloc[:,0:5].std().to_frame().T)


# In[49]:


pd.DataFrame(income_df.iloc[:,0:4].var().to_frame()).T


# In[50]:


income_df["Highest_Qualified_Member"].value_counts()


# In[51]:


income_df["Highest_Qualified_Member"].value_counts().to_frame()


# In[52]:


income_df["Highest_Qualified_Member"].value_counts().to_frame().T


# In[53]:


income_df["No_of_Earning_Members"].value_counts()


# # Plot the Histogram to count the No_of_Earning_Members

# In[54]:


income_df["No_of_Earning_Members"].value_counts().plot(kind="bar")

