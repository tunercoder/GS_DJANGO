
import json
import requests
import json
URL="http://127.0.0.1:8000/stuapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data =  {'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)



def create_data():
    data={
            'name':'kajal',
            'roll':'5',
            'city':'hari'
        }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)



def update_data():
    data={
            'id':4,
            'name':'suanam',
            'city':'del'
        }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)



def delete_data():
    data={
            'id':4
        }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)


# get_data()
# create_data()
# update_data()
delete_data()