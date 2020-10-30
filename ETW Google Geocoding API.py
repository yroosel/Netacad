#!/usr/bin/env python
# coding: utf-8

# In[10]:


#### Google Geocoding API
#### Adapted by Y. Rooseleer, BIASC
#### => API Calls, Request/Response, Authentication, Data Management/Filtering/Selecting/Transforming

import requests
import datetime
import json
print ("Current date and time: ")
print(datetime.datetime.now())
print('Imported libraries for the script')
print('STARTING Google Geocoding API Example Script')
print('=> API Calls, Request/Response, Authentication, Data Management/Filtering/Selecting/Transforming')
#dir(urllib)
#dir(requests)


# In[2]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Getting input')
#####
address = input("Town or City? ")
                


# In[3]:


import requests
import datetime
import json
print ("Current date and time: ")
print(datetime.datetime.now())
main_api = "https://maps.googleapis.com/maps/api/geocode/json"
api_key = "Get your own key"
uri = main_api+"?"+"key"+"="+api_key+"&"+"address"+"="+address
print('Creating full request')
print(uri)
resp  = requests.get(uri)
print("------1--------")
print(type(resp))
print(dir(resp))
#print(resp.__dict__)
print("------2--------")
print(resp.status_code)
print("------3--------")
print(resp.text)
print("------4--------")
json_data = resp.json()
print(type(json_data))
print("------5--------")
print(json_data)
#print("------6--------")
#str_doc = json.dumps(json_data, indent=4)
#print(str_doc)


# In[5]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Success of the request')
print("STATUS")
print('------1--------')
print(resp.status_code)
print('------2-------')
json_status = json_data["status"]
#print("API Status: " + json_status)
print(json_status)


# In[14]:


print ("Current date and time: ")
print(datetime.datetime.now())
print('Raw result of the request')
if resp.status_code == 200:
    print("RAW RESULT IN JSON - STATUS CODE")
    print(resp.status_code)
if json_status == "OK":
    print("RAW RESULT IN JSON - STATUS TEXT")
    print( json_status )
    print('--------------')
    print(json_data)
    print('--------------')


# In[15]:


print ("Current date and time: ")
print(datetime.datetime.now())
print('Filtered result of the request')
if json_status == "OK":
    print("SELECTED RESULT A ")
    print('------1-------')
    selection = json_data['results'][0]['formatted_address']
    print(selection)
    print('------2--------')
    selection = json_data['results'][0]['geometry']['location']
    print(selection)
    print('------3--------')
    selection = json_data['results'][0]['geometry']['location']['lat']
    print(selection)
    selection = json_data['results'][0]['geometry']['location']['lng']
    print(selection)


# In[16]:


print ("Current date and time: ")
print(datetime.datetime.now())
if json_status == "OK":
    print("SELECTED RESULT B ")
    print('--------------')
    selection1 = json_data['results'][0]['address_components'][0]['long_name']
    selection2 = json_data['results'][0]['address_components'][1]['long_name']
    selection3 = json_data['results'][0]['address_components'][2]['long_name']
    selection4 = json_data['results'][0]['address_components'][3]['long_name']
    print(selection1)
    print(selection2)
    print(selection3)
    print(selection4)
    print('--------------')
    


# In[17]:


print ("Current date and time: ")
print(datetime.datetime.now())
print("SELECTED RESULT C ")
print('--------------')
if json_status == "OK":
    print("LOOPING THROUGH RESULTS")
    for each in json_data["results"][0]["address_components"]:
        print(each["long_name"])
print('--------------')

