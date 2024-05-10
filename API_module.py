import requests



def url_response(id:str):
    id = str(id)
    url  = 'https://reqres.in/api/users/'
    
    response = requests.get(url,str(id))
    return response.status_code

def User_response(id):
    # global url
    url  = 'https://reqres.in/api/users/'
    
    url = url+str(id)
    # id  = 
    response = dict(requests.get(url).json())
    # print(response.json().get('data')[0].get('first_name'))
    # print(type(response.json()))
    # print(type(response.get("data").get('first_name')))
    return dict(response.get("data"))





print(User_response(1))