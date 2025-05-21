import json 

data ='{"company":{"name":"Tech Innovations","address":{"street":"123 Tech Lane","city":"Silicon Valley","state":"CA","postal_code":"94043"},"employees":[{"id":1,"name":"Alice","position":"Software Engineer","contact":{"email":"alice@techinnovations.com","phone":"555-1234"}},{"id":2,"name":"Bob","position":"Data Scientist","contact":{"email":"bob@techinnovations.com","phone":"555-5678"}}]}}'
jsondata = json.loads(data)


try:
    for data in jsondata["company"]:
        print(jsondata["employees"][1]["name"], end="\n")
except:
    print(jsondata["company"]["employees"][0])
finally :
    print("Finally,we included a for loop in our code.")

print(jsondata["company"]["employees"][0]["id"])


## well,  this code giving the output 3 times 
#for data in jsondata["company"]:
#        print(jsondata["company"]["employees"][1]["name"], end="\n")

