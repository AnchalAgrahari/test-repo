import json

data ='{"company":{"name":"Tech Innovations","address":{"street":"123 Tech Lane","city":"Silicon Valley","state":"CA","postal_code":"94043"},"employees":[{"id":1,"name":"Alice","position":"Software Engineer","contact":{"email":"alice@techinnovations.com","phone":"555-1234"}},{"id":2,"name":"Bob","position":"Data Scientist","contact":{"email":"bob@techinnovations.com","phone":"555-5678"}}]}}'
jsondata = json.loads(data)

def company_data():
    print(jsondata["company"],["empolyees"])

def address():
    print(jsondata["company"]["address"])

def empolyees():
    for i in jsondata["company"]["employees"]:
        print(i)

    
def mis():
    print(jsondata["company"])
    print(jsondata["company"]["address"]["street"])
    print(jsondata["company"]["employees"])
    print(jsondata["company"]["employees"][0])
    print(jsondata["company"]["employees"][1]["contact"]["phone"])



if __name__ == "__main__":
    #company_data()
    #address()
    empolyees()
   
