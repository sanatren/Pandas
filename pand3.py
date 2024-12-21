#read json file.
#to json file
#normalize json .
import pandas as pd
import json
data = '{"Employee name":"james","email":"james@gmail.com","job profile":[{"title1":"team lead","title2":"Sr.Developer"}]}'
# Convert the dictionary to a JSON-formatted string
# json_data = json.dumps(data)

print(type(data))
print(pd.read_json(data)) #reading str into json file

print(pd.read_json(data,orient = 'record'))#orient function is used to format the file in different ways.
print(pd.read_json(data,orient = 'index'))#in index order format

print(pd.read_json(data,orient = 'index'))#it indicates that the JSON data is in a split format. In this format, 
                                          #the JSON object is represented as a dictionary with separate keys for index, columns, and data. 
#example
data1 = {
    "index": [0, 1, 2],
    "columns": ["Employee name", "email", "job profile"],
    "data": [
        ["james", "james@gmail.com", [{"title1": "team lead", "title2": "Sr.Developer"}]],
        ["john", "john@gmail.com", [{"title1": "developer", "title2": "Jr.Developer"}]],
        ["alice", "alice@gmail.com", [{"title1": "manager", "title2": "Project Manager"}]],
    ]
}

# Convert the dictionary to a JSON-formatted string
json_data = json.dumps(data1)

# Read JSON data with orient='split' into a DataFrame
df = pd.read_json(json_data, orient='split')

#print(df)

#dataframe to json
td = pd.DataFrame([['a','b'],['1','2']],index = ['R1','R2'],columns = ['C1','C2'])

td.to_json('game.json')#converting to json files

#functions in json for different formats.
td.to_json('game.json',orient='index')#priority given to rows over cols
td.to_json('game.json',orient='columns')#priority to cols
td.to_json('game.json',orient='records')#rows will be neglected in this format
td.to_json('game.json',orient='split')#gives records or each index,dara, columns and rows seperately
#td.to_json('game.json',orient='table') #show typed of data of of elements and feilds and schema.

#from csv to json

td1 = pd.read_csv('student.csv')
td1.to_json('son.json',orient = 'index')
td1.to_json('son.json',orient = 'split')

#normalization of json

# to normalize we need to convert our data from str to list form.
data2 = [{"Employee name":"james","email":"james@gmail.com","job profile":{"title1":"team lead","title2":"Sr.Developer"}}]

print(pd.json_normalize(data2))#converts semi-structured json data into flat table.

#functions in normalization
data3 = [
    {
        "id": 1,
        "name": "Cole Volk",
        "fitness": {"height": 130, "weight": 60},
    },
    {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},
    {
        "id": 2,
        "name": "Faye Raker",
        "fitness": {"height": 130, "weight": 60},
    },
]
pd.json_normalize(data3,max_level=0)#max level allows us enter no.of nested data in a list if max level = 1 then we can visit nested data once if 2 the we can visit nested data inside nested data of list
#if max level = 0 then we canenot visit any nested data and cannot normalizde them.

print(pd.json_normalize(data3,max_level=0))
print(pd.json_normalize(data3,max_level=1))



data4 = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]

#To access the list inside list (nested list) we will use the path and meta way

print(pd.json_normalize(data4,"counties"))#access the list inside list(nested list) only.

print(pd.json_normalize(data4,"counties",["state","shortname","info"]))

print(pd.json_normalize(data4,"counties",["state","shortname",["info",'governor',]]))#accesing  all elements in normalized way of info feild