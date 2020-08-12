'''
@author:    Jean-Christophe Chouinard. 
@role:      Sr. SEO Specialist at SEEK.com.au
@website:   jcchouinard.com
@LinkedIn:  linkedin.com/in/jeanchristophechouinard/ 
@Twitter:   twitter.com/@ChouinardJC

Learn Python for SEO
jcchouinard.com/python-for-seo

Get API Keys
jcchouinard.com/how-to-get-google-search-console-api-keys/

How to format your request
jcchouinard.com/what-is-google-search-console-api/
'''

import matplotlib.pyplot as plt
import pandas as pd

import file_manip as fm

site = 'https://www.jcchouinard.com'
filename = 'gsc_data.csv'

df = fm.return_df(site,filename) # Reads all Saved CSVs
r = r'.*python.*'
df['query_type'] = ''
df['query_type'][df['query'].str.contains(r,regex=True)] = 'Python'
df['query_type'][~df['query'].str.contains(r,regex=True)] = 'Not-Python'

t = df.groupby(['date','query_type'])['clicks'].sum().reset_index()
t = t.set_index(['date','query_type'])['clicks'].unstack()
t = t.reset_index().rename_axis(None, axis=1)
t = fm.date_to_index(t,'date')
t.plot(subplots=True,
        sharex=True,
        figsize=(6,6),
        sharey=False)
plt.title('Python VS Non-python Related Keywords')
plt.show()