#!/usr/bin/env python
# coding: utf-8

# # Importing the data

# In[1]:


get_ipython().system('gdown https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/000/940/original/netflix.csv')


# In[4]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


data = pd.read_csv('netflix.csv')


# In[6]:


data.shape


# In[7]:


data.info()


# In[8]:


# taking the copy of data

data_copy = data


# In[9]:


data_copy.head()


# # Un-nesting Cast and Liste_In Columns

# In[84]:


data_copy[['cast','listed_in','country']]=data_copy[['cast','listed_in','country']].apply(lambda X : X.str.split(','))


# In[85]:


data_copy.head()


# In[86]:


data_copy=data_copy.explode('cast').explode('listed_in').explode('country').reset_index(drop=True)


# In[87]:


data_copy.shape


# In[88]:


data_copy.head(10)


# # Handling Null Values

# In[89]:


# Checking Categorical Columns
data_copy['type'].isnull().sum()


# In[90]:


data_copy['title'].isnull().sum()


# In[91]:


data_copy['director'].isnull().sum()


# In[92]:


data_copy['director']=data_copy['director'].fillna('Unknown Director')


# In[93]:


data_copy['director'].isnull().sum()


# In[94]:


data_copy['cast'].isnull().sum()


# In[95]:


data_copy['cast']=data_copy['cast'].fillna('Unknown Actor')


# In[96]:


data_copy['cast'].isnull().sum()


# In[97]:


data_copy['country'].isnull().sum()


# In[98]:


data_copy['country']=data_copy['country'].fillna('Unknown Country')


# In[99]:


data_copy['country'].isnull().sum()


# In[100]:


# Cheking Continous Variables


# In[101]:


data_copy['release_year'].isnull().sum()


# # 1)Find the counts of each categorical variable both using graphical and non- graphical analysis.
# 

# ## Non-Graphical Analysis

# In[102]:


Type_of_Movies = data_copy['type'].value_counts()


# In[103]:


Type_of_Movies


# In[104]:


Movies_released_by_Year=data_copy['release_year'].value_counts()


# In[105]:


Movies_released_by_Year


# In[106]:


Movies_released_by_Country=data_copy['country'].value_counts()


# In[107]:


Movies_released_by_Country


# In[108]:


moveis_by_Genre = data_copy['listed_in'].value_counts()


# In[109]:


moveis_by_Genre


# ## For Graphical Analysis

# In[110]:


sns.countplot(data=data_copy,x='type',order=Type_of_Movies.index)
plt.title('Movies by Type')
plt.show()


# In[111]:


# The length of Genra is big is only showing first 10
sns.countplot(data=data_copy,x='listed_in',order=moveis_by_Genre.iloc[:10].index)
plt.title('Movies by Genre')
plt.xticks(rotation = 90)
plt.show()


# In[112]:


# The length of countries is big is only showing first 10
sns.countplot(data=data_copy,x='country',order=Movies_released_by_Country.iloc[:10].index)
plt.title('Movies released by Country')
plt.xticks(rotation = 90)
plt.show()


# In[113]:


# The length of movies released by each year is big is only showing first 10
sns.countplot(data=data_copy,x='release_year',order=Movies_released_by_Year.iloc[:10].index)
plt.title('Movies released by Year')
plt.xticks(rotation = 90)
plt.show()


# # 2. Comparison of tv shows vs. movies.

# ## a. Find the number of movies produced in each country and pick the top 10 Countries
# 

# In[172]:


Movies = data_copy[data_copy['type']=='Movie']


# In[173]:


Movies.shape


# In[174]:


Movies['country']=Movies['country'].apply(lambda x : x.strip())


# In[158]:


Tv_Shows = data_copy[data_copy['type']=='TV Show']


# In[159]:


Tv_Shows.shape


# In[153]:


Movies.groupby(by='country',sort=False)['title'].count()


# In[154]:


# Since unknow country has 5708 we are droping it
Movies = Movies[Movies['country'] != 'Unknown Country']


# In[155]:


Top_10_Movies_Produced_EachCountry=Movies.groupby(by='country',sort=False)['title'].count().sort_values(ascending = False).iloc[:10]


# In[156]:


Top_10_Movies_Produced_EachCountry


# ## b. Find the number of Tv-Shows produced in each country and pick the top 10 countries.

# In[160]:


Tv_Shows.shape


# In[161]:


Tv_Shows['country']=Tv_Shows['country'].apply(lambda x : x.strip())


# In[162]:


Tv_Shows.groupby(by='country')['title'].count().sort_values(ascending = False)


# In[163]:


# Since Unknown Country has 5437 removing those rows

Tv_Shows=Tv_Shows[Tv_Shows['country']!='Unknown Country']


# In[164]:


Tv_Shows.groupby(by='country')['title'].count().sort_values(ascending = False)


# In[165]:


Top10TvShowsbyCountry=Tv_Shows.groupby(by='country')['title'].count().sort_values(ascending = False).iloc[:10]


# In[167]:


Top10TvShowsbyCountry


# # 3. What is the best time to launch a TV show?

# ## a. Find which is the best week to release the Tv-show or the movie. Do the analysis separately for Tv-shows and Movies
# 

# In[168]:


Movies.head()


# In[181]:


Movies['date_added']=pd.to_datetime(Movies['date_added'])


# In[179]:


Movies.head()


# In[184]:


Movies['Month'] = Movies['date_added'].dt.month_name()


# In[197]:


# When I ran first time the warning was not came but i tried running at again then the warning message showed up


# In[185]:


Movies.head()


# In[201]:


Movies['Week'] = Movies['date_added'].dt.isocalendar().week 


# In[202]:


Movies.head()


# In[203]:


Top_10_weeks_to_Release_Movies=Movies.groupby(by='Week')['title'].count().sort_values(ascending = False).iloc[:10]


# In[204]:


Top_10_weeks_to_Release_Movies


# In[205]:


Tv_Shows.shape


# In[206]:


Tv_Shows['date_added']=pd.to_datetime(Tv_Shows['date_added'])


# In[207]:


Tv_Shows['Month'] = Tv_Shows['date_added'].dt.month_name()


# In[208]:


Tv_Shows['Week'] = Tv_Shows['date_added'].dt.isocalendar().week 


# In[209]:


Tv_Shows


# In[211]:


Top_10_weeks_to_Release_TvShows=Tv_Shows.groupby(by='Week')['title'].count().sort_values(ascending = False).iloc[:10]


# In[212]:


Top_10_weeks_to_Release_TvShows


# ## b. Find which is the best month to release the Tv-show or the movie. Do the analysis separately for Tv-shows and Movies

# In[215]:


TvShowsReleasedByMonth=Tv_Shows.groupby(by='Month')['title'].count().sort_values(ascending = False)


# In[216]:


TvShowsReleasedByMonth


# In[218]:


MoviesReleasedByMonth=Movies.groupby(by='Month')['title'].count().sort_values(ascending = False)


# In[219]:


MoviesReleasedByMonth


# ## 4. Analysis of actors/directors of different types of shows/movies.

# ## a. Identify the top 10 directors who have appeared in most movies or TV shows.
# 

# In[223]:


data_copy['cast']=data_copy['cast'].apply(lambda x :x.strip())


# In[224]:


data_copy['cast'].unique()


# In[228]:


Top10Actors=data_copy.groupby(by='cast')['title'].count().sort_values(ascending = False).iloc[:11]


# In[229]:


Top10Actors


# ##  b. Identify the top 10 Actors who have appeared in most movies or TV shows.

# In[230]:


data_copy['director']=data_copy['director'].apply(lambda x :x.strip())


# In[231]:


data_copy['director'].unique()


# In[233]:


Top10Directors=data_copy.groupby(by='director')['title'].count().sort_values(ascending = False).iloc[:11]


# In[234]:


Top10Directors


# In[235]:


data_copy.head()


# In[236]:


pip install pandas wordcloud matplotlib


# In[238]:


data_genre=data_copy['listed_in']


# In[246]:


data_genre=data_genre.to_frame()


# In[248]:


data_genre['listed_in']=data_genre['listed_in'].apply(lambda x : x.strip())


# In[251]:


data_genre['listed_in'].unique()


# In[256]:


data_genre['listed_in'].value_counts().iloc[:15]


# In[257]:


genre = ','.join(data_genre['listed_in'])


# In[260]:


from wordcloud import WordCloud


# In[272]:


wordcloud = WordCloud(width=800, height=400, background_color='white').generate(genre)


# In[273]:


plt.figure(figsize=(12, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# # 6. Find After how many days the movie will be added to Netflix after the release of the movie (you can consider the recent past data)
# 

# In[289]:


data_copy['date_added']=pd.to_datetime(data_copy['date_added'])


# In[290]:


data_copy['release_year']=pd.to_datetime(data_copy['release_year'], format='%Y')


# In[291]:


data_copy.head()


# In[299]:


data_copy['date_diff']=(data_copy['date_added']-data_copy['release_year']).dt.days


# In[302]:


data_copy['date_diff'].mode()


# In[303]:


data_copy.shape


# In[305]:


data.shape


# In[306]:


# I am performing the same operation on Original data


# In[307]:


data['date_added']=pd.to_datetime(data['date_added'])


# In[308]:


data['release_year']=pd.to_datetime(data['release_year'], format='%Y')


# In[309]:


data['date_diff']=(data['date_added']-data['release_year']).dt.days


# In[313]:


data['date_diff'].mode()


# In[314]:


data['description'].iloc[0]


# # My Analysis

# ## 1) 334 days is the best time to release move into OTT Platform
# ## 2) Drama is the Genre most of the movies Produced
# ## 3) Amupam Kher and Sharukh Khan are the ones who acted in more number of movies
# ## 4) Martin Martin Scorsese and Youssef Chahine are the directors who directed more numner of movies
# ## 5)December is the best time to release Tv Shows and July is best for Movies
# ## 6)week 1 is best for Movies and week 27 is best for Tv Shows
# ## 7) USA and Japan are the countries who produced more number of Tv Shows
# ## 8)USA and India are the countries who Produced more number of Movies

# In[316]:


pip install "nbconvert[webpdf]"


# In[ ]:




