#!/usr/bin/env python
# coding: utf-8

# In[13]:


#### DNA Center => Manage Enterprise Networks and Devices
#### Adapted by Y. Rooseleer, BIASC
#STEP 1 => DEFINE HARD CODED VARIABLES TO BE USED IN THE SCRIPT
import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting DNA Center Hello World - Simple')
print('Creating Hard Coded Variables')

# HARD CODED VARIABLES
DNAC_scheme = 'https://'
DNAC_authority='sandboxdnac.cisco.com'
DNAC_port=':443'
DNAC_path_token='/dna/system/api/v1/auth/token'
DNAC_path='/dna/intent/api/v1/network-device'
DNAC_user='devnetuser'
DNAC_psw='Cisco123!'


# In[16]:


#STEP 2 => REQUEST TOKEN BASED ON USERNAME AND PASSWORD
print ("Current date and time: ")
print(datetime.datetime.now())
print('Post First Request - Token')
# FIRST REQUEST
token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
print(token_req_url)
req = requests.request('POST', token_req_url, auth=(DNAC_user, DNAC_psw), verify=False)
#req = requests.post(token_req_url, auth=(DNAC_user, DNAC_psw), verify=False)
print(req)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
token = req.json()['Token']
print("Received Token:")
print(token)


# In[17]:


#STEP 3 => REQUEST API SERVICE (USING X-AUTH-TOKEN FROM STEP 2)
print ("Current date and time: ")
print(datetime.datetime.now())
print('Second Request - Network Devices')
# SECOND REQUEST
req_url = DNAC_scheme+DNAC_authority+DNAC_port+DNAC_path
print(req_url)
headers = {'X-auth-token': token}
resp_devices = requests.request('GET', req_url, headers=headers, verify=False)
print(resp_devices)
resp_devices_json = resp_devices.json()
print("Respone (json):")
print(json.dumps(resp_devices_json, indent=4))


# In[5]:


#STEP 4 => RETURNED DATA => FILTERING AND LOOPING
print ("Current date and time: ")
print(datetime.datetime.now())
print('Second Request - Providing simple output')
#OUTPUT
for device in resp_devices_json['response']:
    if device['type'] != None:
        print('-Hostname: '+device['hostname']+' --Type: '+device['type']+' ---IP: '+device['managementIpAddress'])


# In[6]:


#STEP 5 => FILTERING JSON DATA 
print ("Current date and time: ")
print(datetime.datetime.now())
print('Second Request - Providing  output in JSON')
#CREATE EMPTY LIST
dev_list = []
for device in resp_devices_json['response']:
    if device['type'] != None:
        #CREATE EMPTY DICT
        dev_dict = {}
        dev_dict['hostname'] = device['hostname']
        dev_dict['type'] = device['type']
        dev_dict['managementIpAddress'] = device['managementIpAddress']
        dev_list.append(dev_dict)
#print(dev_list)     
print(json.dumps(dev_list, indent=2))


# In[18]:


from tabulate import *
print(type(dev_list))
print(tabulate(dev_list))

