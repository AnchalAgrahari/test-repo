import json

def create_table(file_name):
    data = {
        "student_details" : [
            {"Name":"Anchal","age":20,"cource":"B-Tech"},
            {"name":"Mahi","age":20,"course":"BBA"},
            {"name":"Gungun","age":19,"course":"B-Tech"}
        ]
    }

    with open(file_name + ".json","w") as f:
      json.dump(data,f,indent=4)
    print(f"Data written to {file_name}.json")

if __name__ == '__main__':
    try:
        file_name = "JSON.TABLE"
        create_table(file_name)
    except Exception as e:
        print("An Exception occured")
        