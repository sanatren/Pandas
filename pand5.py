#read_xml
#read_xml path
import pandas as pd

print(pd.read_xml('sample.xml'))

xml = '''<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
 <row>
   <shape>square</shape>
   <degrees>360</degrees>
   <sides>4.0</sides>
   <firstname>Krish</firstname>
 </row>
 <row>
   <shape>circle</shape>
   <degrees>360</degrees>
   <sides/>
   <firstname/>
 </row>
 <row>
   <shape>triangle</shape>
   <degrees>180</degrees>
   <sides>3.0</sides>
   <firstname/>
 </row>
</data>'''
td1 = pd.read_xml(xml)
print(type(td1))

#td2 = pd.read_xml(xml,xpath=".//row") used to consider such given feild as tags and create table according to it.
#we wont be able to use it since it is using refrence in xlmns form so we will require anothor feild i.e namespace

#namespace
td2 = pd.read_xml(xml,xpath=".//doc:row",namespaces={"doc":"http://example.com"}) 

print(td2)

td2.to_xml('test1.xml')