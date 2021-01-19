#!/usr/bin/env python
# coding: utf-8

# # Data Exploration

# ## Import Data

# I am using data published in the [OxCGRT USA-covid-policy](https://github.com/OxCGRT/USA-covid-policy/blob/master/data/OxCGRT_US_latest.csv) GitHub.
# 
# I  downloaded the CSV file to my computer and uploaded a version of the data to "Individual Assigment UP 206A" folder. I will be using this file for today's exploration. 

# I first need to import a library that will let read a csv file. Therefore, I will import pandas. 

# In[1]:


import pandas as pd


# I am almost ready to import my data, however, I first need to know the name where my data file is actually store within my jupyterhub. That is why I will run pwd. 

# In[2]:


pwd


# Now that I know where my file is store, I am ready to import. 

# In[3]:


US_policy= pd.read_csv('/home/jovyan/Individual Assignment  UP 206A/OxCGRT_US_latest_1.17.20.csv')


# ## Initial Data Exploration

# Yay! After some struggle(no longer documented in this notebook), I was able to import my data!!! <br> 
# ###### Now, time to start exploring. 

# First, I want to find out what my file data type so I will run the command type() .

# In[4]:


type(US_policy)


# I now know that my file is a DataFrame. I am now interested in learning the shape of my file so I will run the following command so I can know the the number of rows and columns in my data. 

# In[5]:


US_policy.shape


# My file has 69 columns and 20352 rows, wow that's a lot of data! 

# I still want to know more information about my data, so I will run a file that will allow me learn more information.

# In[6]:


US_policy.info


# WOW! That's a lot more information about my data. I can see the first five and last five rows for several variables. 
# It appears the rows at the beginning have information about the US as a whole, and later on, there is data for each state. 
# 
# I can also see a column for "Date", it appears though, that it is possible to examine the data longitudinally. I can see that the first data entry was collected on January 20, 2020 (row 0), and that the latest data entry was collected on January 18, 2021 (row 20351). Given that it's January 17, 2021 (when I am working on this), I am not sure how much I can trust the most recent data for analysis when I am doing the analysis. 
# 
# I also see that there are values for several indexes. I have to use the Github codebook for the [Oxford COVID-19 Codebook](https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md) to that data once I take a closer look later on. 
# 
# 

# To make sure that everything is working, and to get a cleaner look at the first 5 records, I will now run a .head() command

# In[7]:


US_policy.head()


# The head() command produced the information on the first 5 rows of data, with the first and last set of variables presented. However, this time the data looks much cleaner than when I ran the .info command (it is in a table format).

# I am also interested in learning the file types for my data so I will run the .dtype command. 

# In[8]:


US_policy.dtypes


# Thanks to the .dtypes command, I know now that the first five and last five variable types. I know that the first five are objects (or strings), and that the last five are strings (object), and the last five are floating (float64). That makes sense for the last five since I saw above they had decimal values. 

# However, I still don't know the name of all possible variables so I'll run a .columns.to_list command.

# In[9]:


US_policy.columns.to_list()


# Now I can see all of the columns in my data. The first six variables help identify the data's geographical location and the date the data was recorded. Then, several variables seem to provide data on individual policies, such as school closing and investment in vaccines. It also seems like the data set contains confirmed COVID-19 Cases and deaths. Finally, the last set of variables includes Oxford's variables to measure stringency, government response, containment, and economic support. 

# ## Filtering the Dataset 

# Now, I am interested in looking at the data more closely. I believe that the RegionName column is information about which state that the data belongs to. I want to learn more about how much data was collected for each state, so I will run a value_count() command. 

# In[10]:


US_policy.RegionName.value_counts()


# Thanks to running the value_count command for region name, I can see 384 rows for each of the states.

# Now, I also want to get a bit more information about the dates, so I will run the same command for the Date column.

# In[11]:


US_policy['Date'].value_counts()


# Now that I counted the dates' values, it seems like each date has a total of 53 cases associated with it. There must be a date for each of the 50 states and one for the USA, but I am unsure of the last two potential rows for the repeated dates. 

#  Now,  I am going to run a .query command to filter the data by specific data. However, I know that the Date data contains information for values outside of the 50 U.S. I will also filter the data by Jurisdiction to only see the data for the U.S. states (STATE_WIDE). I will pick a random date since I am just trying to test out whether or not my query command works. 

# In[12]:


US_policy.query("(Date == 20200909) & (Jurisdiction == 'STATE_WIDE')")


# I was able to get a table with only state-level data for one date!! Yay! 

# Now, I want to work with a smaller set of my data. I am going to create state_policy which will have a smaller set of columns and only data from states (not the whole country). 

# In[13]:


state_policy=US_policy[['RegionName', 'Date','ConfirmedCases', 'Jurisdiction',
 'ConfirmedDeaths',
 'StringencyIndex',
 'StringencyIndexForDisplay',
 'StringencyLegacyIndex',
 'StringencyLegacyIndexForDisplay',
 'GovernmentResponseIndex',
 'GovernmentResponseIndexForDisplay',
 'ContainmentHealthIndex',
 'ContainmentHealthIndexForDisplay',
 'EconomicSupportIndex',
 'EconomicSupportIndexForDisplay']].query( "(Jurisdiction == 'STATE_WIDE')").copy()
state_policy


# I have selected a smaller set of my data and save it under state_policy. I added a note .copy() to make note that this is a copy of my original data. 

# ## Plots 

# Okay, now I am going to work toward creating a plot. Right now, the table is still presenting a lot of data. I am first going to  import matplotlib.pyplot.

# In[14]:


import matplotlib.pyplot as plt


# Now I have imported a program that will let me create plots for my data. 

# Before I can plot it though, I have to make a new variable with the data I want to plot. I am going to start first with just the stringency index.

# In[15]:


stringency_index=state_policy[['RegionName','Date', 'StringencyIndexForDisplay']]
stringency_index


# I have now created a variable that contatins the name of the state, the date, and the stringency index value. 

# So close to being able to plot my data! However, first, I need to rename my columns so they can show up better on my plots.

# In[16]:


stringency_index.columns = ['State','Date', 'Stringency Index Score']
stringency_index


# The name of my columns has now been updated. 

# Now, it's time to create my first plot. I am going to plot the stringency values for each state for a specific date. I will use the .plot.bar() command to do this.

# In[17]:


stringency_index.query("(Date == 20200909)").plot.bar( figsize=(20,12), x='State', y='Stringency Index Score', title= 'Stringency Index on September 9,2020')


# Great! I created my first plot! I can see each state's names at the bottom and its corresponding Stringency Index value on the y axis. It seems like South Dakota has the lowest index value and that Hawaii has the highest index value. 

# Now, I want to understand the data longitudinally. To do this, I will choose one state, so I can plot out how the score has changed throughout the pandemic. 

# In[18]:


stringency_index.query("(State == 'California')").plot(x='Date', y='Stringency Index Score', title= 'Stringency Index in California')


# Through this plot, I was able to visualize how stringent government coronavirus policies were overtime in California. It appears that Government policies were the most rigorous at the beginning of the pandemic, then lowering a down before they level off around 75.

# Okay, now since I want to better understand my data, I will repeat the steps starting from when I created the stringent_index column to when I made the plot() graph. I will not be explaining my steps on markdown as I do this since it will be the same method. I will do this for COVID-19 Cases and Goverment Response. 

# In[19]:


covid_cases=state_policy[['RegionName','Date', 'ConfirmedCases']]
covid_cases


# In[20]:


covid_cases.columns = ['State','Date', 'COVID-19 Cases']
covid_cases


# In[21]:


covid_cases.query("(Date == 20200909)").plot.bar( figsize=(20,12), x='State', y='COVID-19 Cases', title= 'COVID-19 Cases on September 9,2020')


# In[22]:


covid_cases.query("(State == 'California')").plot(x='Date', y='COVID-19 Cases', title= 'COVID-19 Cases in California')


# In[23]:


gov_response = state_policy[['RegionName','Date', 'GovernmentResponseIndex']]
gov_response


# In[24]:


gov_response.columns = ['State','Date', 'Goverment Response']
gov_response


# In[25]:


gov_response.query("(Date == 20200909)").plot.bar( figsize=(20,12), x='State', y='Goverment Response', title= 'Goverment Response on September 9,2020')


# In[26]:


gov_response.query("State == 'California'").plot(x='Date', y='Goverment Response', title = 'Goverment Response in California')


# I was able to plot both COVID-19 cases and Government Response on September 9, 2020, and over time in California.  I am excited to continue learning more python commands so I can better analyze my data. 

# ## The End 

# ##### Stay tune for more analysis!! 
