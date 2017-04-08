
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index


# In[5]:

pd.Series(np.random.randn(5))


# In[6]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[7]:

d


# In[8]:

pd.Series(d)


# In[9]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[10]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s


# In[13]:

s[0]


# In[14]:

s[:3]


# In[15]:

s[s > s.median()]


# In[16]:

s[s > s.mean()]


# In[17]:

ds = pd.Series(d)
ds.median


# In[18]:

s[[4, 3, 1]]


# In[19]:

# returns exponential of each number in a series
np.exp(s)


# In[20]:

# search by index, because it has a sensful name - Sensible indexing
s['a']


# In[21]:

# set value to a series index
s['e'] = 12


# In[22]:

s


# In[23]:

# if a column doesn't exist, we get an exception
s['f']



# In[27]:

# instead use if in
if 'f' in s:
    print(s['f'])


# In[26]:

s


# In[28]:

'e' in s


# In[29]:

'f' in s


# In[30]:

s.get('e')


# In[32]:

s.get('f')


# In[33]:

s.get('f', np.nan)


# In[34]:

#add and make calculation with series
s+s


# In[35]:

s * 3


# In[36]:

s[1:]


# In[38]:

s[:-1]


# In[39]:

s[1:] + s[:-1]


# In[47]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
  'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[48]:

d


# In[49]:

df = pd.DataFrame(d)


# In[50]:

# creates a spreadsheet
df


# In[51]:

# selecting only some columns in a column
pd.DataFrame(d, index=['d', 'b', 'a'])


# In[52]:

# rename columns and add new empty ones
pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[53]:

df.index


# In[55]:

df.columns


# In[56]:

d = {'one' : [1., 2., 3., 4.],
   'two' : [4., 3., 2., 1.]}


# In[57]:

d


# In[60]:

pd.DataFrame(d)


# In[61]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[62]:

# select the format of content in columns i4 = integer, f4 = numeric, a10 = string of 10 - Here you set to add only 00 in the first 2 columns
## Look for numpy weros function

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[63]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[64]:

pd.DataFrame(data)


# In[65]:

# no column names
data


# In[66]:

pd.DataFrame(data, index=['first', 'second'])


# In[67]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[68]:

# set an empty column
pd.DataFrame(data, columns=['C', 'A', 'B', 'D'])


# In[69]:

mydata = pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[70]:

mydata


# In[71]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[72]:

data2


# In[73]:

pd.DataFrame(data2)


# In[74]:

pd.DataFrame(data2, index=['first', 'second'])


# In[75]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[76]:

df


# In[77]:

df['one']


# In[84]:

# create a column with calculations
df['three'] = df['one'] * df['two']


# In[79]:

df


# In[80]:

# column with boolean content
# if column 1 is > 2
df['flag'] = df['one'] > 2


# In[81]:

df


# In[82]:

# delete columns
del df['two']


# In[85]:

# remove without deleting - u can use the content of a column but don't see it
three = df.pop('three')


# In[86]:

df


# In[87]:

df.loc['a']


# In[88]:

# three exists as an object on its own
three


# In[89]:

df['foo'] = 'bar'


# In[90]:

df


# In[91]:

df['one_trunc'] = df['one'][:2]


# In[92]:

df


# In[93]:

df.insert(1, 'bar', df['one'])

# or 
df['bar'] = df['one']


# In[94]:

df


# In[ ]:



