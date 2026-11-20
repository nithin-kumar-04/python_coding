import json

data='{"name":"Nithin","id":5418}'
#converting json to dict
result=json.loads(data)
print(type(result))
#converting dicy to json
x=json.dumps(result)
print(type(x))



#open repo in github
#name,email,batch-id
#title
#backend program