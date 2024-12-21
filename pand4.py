#read html 
#to html
import pandas as pd

html = pd.read_html('https://en.wikipedia.org/wiki/Mobile_country_code')

#print(html)

print(html[0])#this indexing prints the table according to their appearence in the main file.
print(html[1])

#function to pick or select specific table in html file we will use match function 

html2 = pd.read_html('https://en.wikipedia.org/wiki/Mobile_country_code',match='Remarks')#to use match we need to assign it with row name which is not coomon on any other table of html file.

td1 = html[1]
td1.to_html('demo.html')
print(td1.sort_values(by = 'Mobile country code')) #sorting hmtl table by column name

print(td1.add(html[0])) #adding two dataframes.
#print(td1.replace(to_replace=td1[td1 > 247], value=300))#replacing specific values with 300