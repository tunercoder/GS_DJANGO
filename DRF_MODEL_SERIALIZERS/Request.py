
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
            'name':'ray',
            'roll':'121',
            'city':'ranchi'
        }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)



def update_data():
    data={
            'id':1,
            'name':'roya',
            'roll':111,
            'city':'jamu'
        }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)



def delete_data():
    data={
            'id':2
        }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)


# get_data()
create_data()
# update_data()
# delete_data()