#!/usr/bin/env python
# coding: utf-8

# In[19]:


### Python and JSON Workshop -- Y. Rooseleer <yvan@biasc.be>
### 22 example exercises friltering JSON, dict and list structures
### Part 1: Filtering JSON Data
### 1 ###
### Managing IP Addresses with Python
### json structure already converted to dict
import json
### Data Structures
host               =  {"hostname" : "CSR1kv"}
multiple_hosts     = [{"hostname" : "CSR1kv"}, {"hostname" : "CSR2kv"}, {"hostname" : "CSR3kv"}]
multiple_hostnames = [ "CSR1kv", "CSR2kv", "CSR3kv"]
single_address     =  {'ip': '192.168.56.101', 'netmask': '255.255.255.0'}
multiple_addresses = [{'ip': '192.168.56.101', 'netmask': '255.255.255.0'},
                      {'ip': '192.0.2.1', 'netmask': '255.255.255.252'} ]
ietf_ipv4          =  {'address': [{'ip': '192.168.56.101', 'netmask': '255.255.255.0'} , 
                                   {'ip': '192.0.2.1', 'netmask': '255.255.255.252'} ]}
### Recognize Data Type
print('-----1------')
print(type(host))
print(type(multiple_hosts))
print(type(multiple_hostnames))
print('-----1B-----')
print(host)
print(host["hostname"])
print(multiple_hosts)
print(multiple_hosts[-1]["hostname"])
print(multiple_hostnames[-1])
print('-----2------')
print(type(single_address))
print(type(multiple_addresses))
print(type(ietf_ipv4))
print('-----2B-----')
print(ietf_ipv4['address'])
print(ietf_ipv4['address'][0]['ip'])
print(ietf_ipv4['address'][1]['ip'])


# In[21]:


### 2 ###
### Managing IP Prefixes with Python
### json structure already converted to dict using the variable "prefix_subnet_masks"
prefix_subnet_masks = {
    '/23': '255.255.254.0',    
    '/24': '255.255.255.0',
    '/25': '255.255.255.128',
    '/26': '255.255.255.192',
    '/27': '255.255.255.224',
    '/28': '255.255.255.240',
   }

# example 1 -- using square brackets to select a key
subnet_mask_1 = prefix_subnet_masks['/25']   
print(subnet_mask_1 )    

# example 2 -- using get() function to select a key
subnet_mask_2 = prefix_subnet_masks.get('/25')
print(subnet_mask_2)    


# In[27]:


### 3 ###
### Managing IP Subnets with Python
### json structure already converted to dict using the variable "netmask_prefixes"
netmask_prefixes = {
     '255.255.255.252': '/30'
    ,'255.255.255.248': '/29'
    ,'255.255.255.240': '/28'
    ,'255.255.255.224': '/27'
    ,'255.255.255.192': '/26'
    ,'255.255.255.128': '/25'
    ,'255.255.255.0'  : '/24'
    ,'255.255.254.0'  : '/23'
   }
#print(type(netmask_prefixes))
# Adapt to code fragment below to produce the output given
# Output: /27
Prefix_1 = netmask_prefixes['255.255.255.224']   
print(Prefix_1)    


# In[24]:


### 4 ###
### RESTCONF Filter Response Data
### https://192.168.56.101/restconf/data/ietf-interfaces:interfaces
### Authentication header needed
import json
### json structure already converted to dict using the variable "resp"
resp = {"ietf-interfaces:interfaces": 
        {"interface": [
            {"name": "GigabitEthernet1", "description": "VBox", "type": "iana-if-type:ethernetCsmacd", "enabled": True, 
             "ietf-ip:ipv4": 
             {"address": [{"ip": "192.168.56.101", "netmask": "255.255.255.0"}]}, 
             "ietf-ip:ipv6": {}}, 
            {"name": "Loopback9", "description": "999", "type": "iana-if-type:softwareLoopback", "enabled": True, 
             "ietf-ip:ipv4": 
             {"address": [{"ip": "10.9.9.9", "netmask": "255.255.255.0"},
                          {"ip": "172.29.0.9", "netmask": "255.255.255.0"}]}, "ietf-ip:ipv6": {}
            }
        ]
        }
       }
#print(" => Printing type of the response")
print(type(resp))
print(" => Printing response keys")
print(resp['ietf-interfaces:interfaces']['interface'][0].keys())
#print(ip_info)
#print(json.dumps(ip_info, indent=4))
print(" => Printing filtered response (first interface)")
print("Interface Name: ")
print(resp["ietf-interfaces:interfaces"]["interface"][0]["name"])
print("IP Address + Subnet: " )
ip_subnet = resp["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]["address"] 
print(ip_subnet)
print("IP Addresses (all interfaces): " )
ip1 = resp["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]["address"][0]["ip"]
ip2 = resp["ietf-interfaces:interfaces"]["interface"][1]["ietf-ip:ipv4"]["address"][0]["ip"]
ip3 = resp["ietf-interfaces:interfaces"]["interface"][1]["ietf-ip:ipv4"]["address"][1]["ip"]
print(ip1)
print(ip2)
print(ip3)


# In[29]:


### 5 ###
### Cisco DNA Center API Token
### ‘https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token’
### json structure already converted to dict using the variable "resp"
resp = {"Token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZTlkYmI3NzdjZDQ3ZTAwNGM2N2RkMGUiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCI6IxT1u9Vr9I_pj8EmkC3zIUSx5Hjr__TA-8VG86IGwW5-eTRRYaAcf2g8t6UkMs8Y9aGbfcDRgWfxmJOtPxx4_20J7tQIIgzQ9Iod9xY4UYCg8g6qu1DQuEoikWFLW_lH6aA"}
token = resp["Token"]
print(len(token))
print(token)


# In[1]:


### 6 ###
### DNA Center Response Data - Network Device List
### https://sandboxdnac.cisco.com:443/dna/intent/api/v1/network-device
### Authentication header needed
### json structure already converted to dict using the variable "resp"
resp = {
    "response": [{
        "family": "Switches and Hubs",
        "hostname": "cat_9k_1",
        "macAddress": "f8:7b:20:67:62:80",
        "serialNumber": "FCW2136L0AK",
        "upTime": "25 days, 19:42:18.12",
        "softwareType": "IOS-XE",
        "softwareVersion": "17.3.1",
        "bootDateTime": "2020-12-24 17:11:54",
        "managementIpAddress": "10.10.22.66",
        "platvormId": "C9300-24UX",
        "reachabilityStatus": "Reachable",
        "series": "Cisco Catalyst 9300 Series Switches",
        "type": "Cisco Catalyst 9300 Switch",
        "role": "ACCESS",
        "instanceUuid": "21335daf-f5a1-4e97-970f-ce4eaec339f6",
        "id": "21335daf-f5a1-4e97-970f-ce4eaec339f6"
    }],
    "version": "1.0"
}
#print(resp)
dev_list = []   #create empty list
# looping through results and filter needed information
# creating new JSON structure
for device  in resp['response']:
    if device['type'] != None:
        dev_dict = {} #create empty dict
        dev_dict['hostname'] = device['hostname']
        dev_dict['managementIpAddress'] = device['managementIpAddress']
        dev_dict['softwareType'] = device['softwareType']
        dev_dict['softwareVersion'] = device['softwareVersion']
        dev_dict['reachabilityStatus'] = device['reachabilityStatus']
        dev_list.append(dev_dict)
#print(dev_dict)
print('--------1--------')
print("Printing Keys")
for k in dev_dict.keys():
    print(k)
#print(dir(dev_dict))
print('--------2--------')
print("Printing Keys and Values")
for k,v in dev_dict.items():
    print(k + " ==> " + v )


# In[31]:


### 7 ###
### DNA Center Response Data - Client Health
### resp = requests.get( f"https://{host}/dna/intent/api/v1/client-health", headers=headers, params=params )
### json structure already converted to dict using the variable "resp"
resp = {'response': [{'siteId': 'global', 'scoreDetail': [{'scoreCategory': {'scoreCategory': 'CLIENT_TYPE', 'value': 'ALL'}, 'scoreValue': 29, 'clientCount': 82, 'clientUniqueCount': 82, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'CLIENT_TYPE', 'value': 'WIRED'}, 'scoreValue': 100, 'clientCount': 2, 'clientUniqueCount': 2, 'starttime': 1611071700000, 'endtime': 1611072000000, 'scoreList': [{'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'POOR'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'FAIR'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'GOOD'}, 'scoreValue': -1, 'clientCount': 2, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000, 'scoreList': [{'scoreCategory': {'scoreCategory': 'deviceType', 'value': 'ALL'}, 'scoreValue': -1, 'clientCount': 2, 'clientUniqueCount': None, 'starttime': 1611071700000, 'endtime': 1611072000000}]}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'IDLE'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'NODATA'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'NEW'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}]}, {'scoreCategory': {'scoreCategory': 'CLIENT_TYPE', 'value': 'WIRELESS'}, 'scoreValue': 28, 'clientCount': 80, 'clientUniqueCount': 80, 'starttime': 1611071700000, 'endtime': 1611072000000, 'scoreList': [{'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'POOR'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'FAIR'}, 'scoreValue': -1, 'clientCount': 58, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000, 'scoreList': [{'scoreCategory': {'scoreCategory': 'deviceType', 'value': 'ALL'}, 'scoreValue': -1, 'clientCount': 58, 'clientUniqueCount': None, 'starttime': 1611071700000, 'endtime': 1611072000000}]}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'GOOD'}, 'scoreValue': -1, 'clientCount': 22, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000, 'scoreList': [{'scoreCategory': {'scoreCategory': 'deviceType', 'value': 'ALL'}, 'scoreValue': -1, 'clientCount': 22, 'clientUniqueCount': None, 'starttime': 1611071700000, 'endtime': 1611072000000}]}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'IDLE'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'NODATA'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}, {'scoreCategory': {'scoreCategory': 'SCORE_TYPE', 'value': 'NEW'}, 'scoreValue': -1, 'clientCount': 0, 'clientUniqueCount': 0, 'starttime': 1611071700000, 'endtime': 1611072000000}]}]}]}
print(type(resp))
print("Number of clients in first group")
print(resp["response"][0]["scoreDetail"][0]["clientCount"])


# In[32]:


### 8 ###
### Webex Response Data /people/me Python => True/False  JSON: true/false
### https://api.ciscospark.com/v1/people/me
### json structure already converted to dict using the variable "resp"
resp = {"id":"Y2lzY29zcGFya...NlYzQ5NjI5MGY","emails":["Yvan.rooseleer@biasc.be"],"sipAddresses":[{"type":"personal-room","value":"838744612@biasc.webex.com","primary":False},{"type":"personal-room","value":"yvan.rooseleer@biasc.webex.com","primary":False},{"type":"cloud-calling","value":"Yvan.rooseleer@biasc.calls.webex.com","primary":True}],"displayName":"Yvan Rooseleer","nickName":"Yvan","firstName":"Yvan","lastName":"Rooseleer","avatar":"https://avatar-prod-us-east-2.webexcontent.com/Avtr~V1~e4d4112d-2548-4a47-810e-04fe64-a79b-49c5-823a-92cec494bb9c1d1de6~1600","orgId":"Y2lzY29zcGFyazovL3VzL09SR0FOSctODEwZS0wNGZlNDVlYTE4MWY","roles":["Y2lzY29zcGFya9hZG1pbg"],"licenses":["Y2lTQtNDExMS1hYThkLTA1MDI3N2Y3ZjdlOQ","Y2lzY29zcGFyazovL3VzL0xJQ0VOy53ZWJleC5jb20","Y2lzY29zcGFyazovL3VzL0xJQ0VOUxYmJlNTU2LWQwZmItNGFiNy1hMTYyLTlmNjQ2OGIyYmU5ZA","Y2lzYVOU0UvZTRkNDExMmQtMjU0OC00MWBiNDI4MmQ5NmY5NA","Y2lzYTJhNTNfYmlhc2Mud2ViZXguY29t","Y2lzYZWExODFmOkZTU18xYjcyOGZmOS03ZGU4LTRjYjctOTU0MC0yOTMyMGI1YTQyY2I","Y2lzY29zUtMDRmZTQ1ZWExODFmOkZUTV9mNWZkZTM1Zi00NzA0LTQ2MGEtODEwZi00YzVkMzUyNDFlNjk","Y2lzY29zcExODFmOkNHXzVkYjcwNjYyLWNmYTItNGFjZC04MTRlLTgwYjNiNWVkZjNlZA","Y2lzY29zcGFyazovL3jQ3MzgyOC1hOTgwLTQ3MmYtODE5ZC02YjljY2UwOGU5MmI","Y2lzY29zcGFyazovLmOkZNU185ZWNhNzgxNC0zMzEzLTQ2NGYtOTY0Mi0wMjM5ODc1YmM5Zjg","Y2lzY29zcGFyazovLNDExMmQtMjU0OGE3NS1hNDNmLTBkYmJhMjIyNzg3Zl9iaWFzYy53ZWJleC5jb20","Y2lMwMjFkLTgwYjctNDFiYi1iZThhLWM0YjFiZjcyNTE4YV9iaWFzYy53ZWJleC5jb20","Y2lzY29zcGFyazovL3V0YTQ3LTgxMGUtMDRmZTQ1ZWExODFmOk1kYmFiMDcxYmY0NA","Y2lzY29zcGFyazovL3VzL0xJQ0VOUXzNkMDU3N2RiLTFjOGItNDQ4My1hMTBjLzYy53ZWJleC5jb20"],"created":"2016-12-23T08:38:22.877Z","lastModified":"2021-01-26T17:55:07.662Z","lastActivity":"2021-01-26T17:54:24.481Z","status":"active","invitePending":False,"loginEnabled":True,"type":"person","trainSiteNames":["biasc.webex.com"]}
print("Displaying partial information")
print("Name: " + resp['displayName'])
print("Created: " + resp['created'])
print("User Type: " + resp['type'])
print("User Status: " + resp['status'])


# In[33]:


### 9 ###
### Ansible Response Data --- very long --------------------------------------
### $ ansible webservers -m gather_facts --tree ./tmp_facts
### External file can be downloaded here: https://docs.google.com/document/d/1Z7wO5r8XaBirxXo06CmC8a6r5cCMezQQqUOcHxXhCyk/edit?usp=sharing
### json structure already converted to dict using the variable "resp"
resp =  {"ansible_facts": {"ansible_all_ipv4_addresses": ["192.0.2.1", "192.0.2.2", "192.0.2.3", "192.0.2.4", "192.0.2.5", "10.0.2.15", "172.17.0.1"], "ansible_all_ipv6_addresses": ["fe80::9002:c8ff:fee8:bb09", "fe80::3c67:a5ff:fe17:e4cf", "fe80::a00:27ff:fee9:3de6", "fe80::42:3ff:fef6:9477"], "ansible_apparmor": {"status": "enabled"}, "ansible_architecture": "x86_64", "ansible_bios_date": "12/01/2006", "ansible_bios_version": "VirtualBox", "ansible_cmdline": {"BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic", "quiet": True, "ro": True, "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9", "vga": "792", "zswap.enabled": "1"}, "ansible_date_time": {"date": "2021-01-27", "day": "27", "epoch": "1611765624", "hour": "16", "iso8601": "2021-01-27T16:40:24Z", "iso8601_basic": "20210127T164024318962", "iso8601_basic_short": "20210127T164024", "iso8601_micro": "2021-01-27T16:40:24.319071Z", "minute": "40", "month": "01", "second": "24", "time": "16:40:24", "tz": "UTC", "tz_offset": "+0000", "weekday": "Wednesday", "weekday_number": "3", "weeknumber": "04", "year": "2021"}, "ansible_default_ipv4": {"address": "10.0.2.15", "alias": "enp0s3", "broadcast": "10.0.2.255", "gateway": "10.0.2.2", "interface": "enp0s3", "macaddress": "08:00:27:e9:3d:e6", "mtu": 1500, "netmask": "255.255.255.0", "network": "10.0.2.0", "type": "ether"}, "ansible_default_ipv6": {}, "ansible_device_links": {"ids": {"sda": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"], "sda1": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"], "sda2": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part2"], "sda5": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part5"]}, "labels": {}, "masters": {}, "uuids": {"sda1": ["AF29-5078"], "sda5": ["fb261367-cf98-4bce-b682-42b3de0a8ab9"]}}, "ansible_devices": {"loop0": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "113424", "sectorsize": "512", "size": "55.38 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop1": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "299016", "sectorsize": "512", "size": "146.00 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop10": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "333552", "sectorsize": "512", "size": "162.87 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop11": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "359216", "sectorsize": "512", "size": "175.40 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop12": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "132648", "sectorsize": "512", "size": "64.77 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop13": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "242568", "sectorsize": "512", "size": "118.44 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop14": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "131792", "sectorsize": "512", "size": "64.35 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop15": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "330576", "sectorsize": "512", "size": "161.41 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop16": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "0", "sectorsize": "512", "size": "0.00 Bytes", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop17": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "200464", "sectorsize": "512", "size": "97.88 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop18": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "189312", "sectorsize": "512", "size": "92.44 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop2": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "300120", "sectorsize": "512", "size": "146.54 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop3": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "496912", "sectorsize": "512", "size": "242.63 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop4": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "294528", "sectorsize": "512", "size": "143.81 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop5": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "359032", "sectorsize": "512", "size": "175.31 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop6": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "200416", "sectorsize": "512", "size": "97.86 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop7": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "277848", "sectorsize": "512", "size": "135.67 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop8": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "191232", "sectorsize": "512", "size": "93.38 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "loop9": {"holders": [], "host": "", "links": {"ids": [], "labels": [], "masters": [], "uuids": []}, "model": "", "partitions": {}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "113384", "sectorsize": "512", "size": "55.36 MB", "support_discard": "4096", "vendor": "", "virtual": 1}, "sda": {"holders": [], "host": "IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)", "links": {"ids": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"], "labels": [], "masters": [], "uuids": []}, "model": "VBOX HARDDISK", "partitions": {"sda1": {"holders": [], "links": {"ids": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"], "labels": [], "masters": [], "uuids": ["AF29-5078"]}, "sectors": "1048576", "sectorsize": 512, "size": "512.00 MB", "start": "2048", "uuid": "AF29-5078"}, "sda2": {"holders": [], "links": {"ids": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part2"], "labels": [], "masters": [], "uuids": []}, "sectors": "2", "sectorsize": 512, "size": "1.00 KB", "start": "1052670", "uuid": ""}, "sda5": {"holders": [], "links": {"ids": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part5"], "labels": [], "masters": [], "uuids": ["fb261367-cf98-4bce-b682-42b3de0a8ab9"]}, "sectors": "64481280", "sectorsize": 512, "size": "30.75 GB", "start": "1052672", "uuid": "fb261367-cf98-4bce-b682-42b3de0a8ab9"}}, "removable": "0", "rotational": "1", "sas_address": "", "sas_device_handle": "", "scheduler_mode": "mq-deadline", "sectors": "65536000", "sectorsize": "512", "size": "31.25 GB", "support_discard": "0", "vendor": "ATA", "virtual": 1}}, "ansible_distribution": "Ubuntu", "ansible_distribution_file_parsed": True, "ansible_distribution_file_path": "/etc/os-release", "ansible_distribution_file_variety": "Debian", "ansible_distribution_major_version": "20", "ansible_distribution_release": "focal", "ansible_distribution_version": "20.04", "ansible_dns": {"nameservers": ["127.0.0.53"], "options": {"edns0": True}, "search": ["telenet.be"]}, "ansible_docker0": {"active": True, "device": "docker0", "features": {"esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "fcoe_mtu": "off [fixed]", "generic_receive_offload": "on", "generic_segmentation_offload": "on", "highdma": "on", "hw_tc_offload": "off [fixed]", "l2_fwd_offload": "off [fixed]", "large_receive_offload": "off [fixed]", "loopback": "off [fixed]", "netns_local": "on [fixed]", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "rx_all": "off [fixed]", "rx_checksumming": "off [fixed]", "rx_fcs": "off [fixed]", "rx_gro_hw": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "rx_vlan_filter": "off [fixed]", "rx_vlan_offload": "off [fixed]", "rx_vlan_stag_filter": "off [fixed]", "rx_vlan_stag_hw_parse": "off [fixed]", "scatter_gather": "on", "tcp_segmentation_offload": "on", "tls_hw_record": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_ip_generic": "on", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_sctp": "off [fixed]", "tx_checksumming": "on", "tx_esp_segmentation": "on", "tx_fcoe_segmentation": "off [requested on]", "tx_gre_csum_segmentation": "on", "tx_gre_segmentation": "on", "tx_gso_partial": "on", "tx_gso_robust": "off [requested on]", "tx_ipxip4_segmentation": "on", "tx_ipxip6_segmentation": "on", "tx_lockless": "on [fixed]", "tx_nocache_copy": "off", "tx_scatter_gather": "on", "tx_scatter_gather_fraglist": "on", "tx_sctp_segmentation": "on", "tx_tcp6_segmentation": "on", "tx_tcp_ecn_segmentation": "on", "tx_tcp_mangleid_segmentation": "on", "tx_tcp_segmentation": "on", "tx_udp_segmentation": "on", "tx_udp_tnl_csum_segmentation": "on", "tx_udp_tnl_segmentation": "on", "tx_vlan_offload": "on", "tx_vlan_stag_hw_insert": "on", "vlan_challenged": "off [fixed]"}, "hw_timestamp_filters": [], "id": "8000.024203f69477", "interfaces": ["vethacd0508"], "ipv4": {"address": "172.17.0.1", "broadcast": "172.17.255.255", "netmask": "255.255.0.0", "network": "172.17.0.0"}, "ipv6": [{"address": "fe80::42:3ff:fef6:9477", "prefix": "64", "scope": "link"}], "macaddress": "02:42:03:f6:94:77", "mtu": 1500, "promisc": False, "stp": False, "timestamping": ["rx_software", "software"], "type": "bridge"}, "ansible_domain": "vm", "ansible_dummy0": {"active": True, "device": "dummy0", "features": {"esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "fcoe_mtu": "off [fixed]", "generic_receive_offload": "on", "generic_segmentation_offload": "on", "highdma": "on", "hw_tc_offload": "off [fixed]", "l2_fwd_offload": "off [fixed]", "large_receive_offload": "off [fixed]", "loopback": "off [fixed]", "netns_local": "on [fixed]", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "rx_all": "off [fixed]", "rx_checksumming": "off [fixed]", "rx_fcs": "off [fixed]", "rx_gro_hw": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "rx_vlan_filter": "off [fixed]", "rx_vlan_offload": "off [fixed]", "rx_vlan_stag_filter": "off [fixed]", "rx_vlan_stag_hw_parse": "off [fixed]", "scatter_gather": "on", "tcp_segmentation_offload": "on", "tls_hw_record": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_ip_generic": "on", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_sctp": "off [fixed]", "tx_checksumming": "on", "tx_esp_segmentation": "on", "tx_fcoe_segmentation": "on", "tx_gre_csum_segmentation": "on", "tx_gre_segmentation": "on", "tx_gso_partial": "on", "tx_gso_robust": "on", "tx_ipxip4_segmentation": "on", "tx_ipxip6_segmentation": "on", "tx_lockless": "on [fixed]", "tx_nocache_copy": "off", "tx_scatter_gather": "on", "tx_scatter_gather_fraglist": "on", "tx_sctp_segmentation": "on", "tx_tcp6_segmentation": "on", "tx_tcp_ecn_segmentation": "on", "tx_tcp_mangleid_segmentation": "on", "tx_tcp_segmentation": "on", "tx_udp_segmentation": "on", "tx_udp_tnl_csum_segmentation": "on", "tx_udp_tnl_segmentation": "on", "tx_vlan_offload": "on", "tx_vlan_stag_hw_insert": "on", "vlan_challenged": "off [fixed]"}, "hw_timestamp_filters": [], "id": "8000.000000000000", "interfaces": [], "ipv4": {"address": "192.0.2.1", "broadcast": "global", "netmask": "255.255.255.255", "network": "192.0.2.1"}, "ipv4_secondaries": [{"address": "192.0.2.2", "broadcast": "global", "netmask": "255.255.255.255", "network": "192.0.2.2"}, {"address": "192.0.2.3", "broadcast": "global", "netmask": "255.255.255.255", "network": "192.0.2.3"}, {"address": "192.0.2.4", "broadcast": "global", "netmask": "255.255.255.255", "network": "192.0.2.4"}, {"address": "192.0.2.5", "broadcast": "global", "netmask": "255.255.255.255", "network": "192.0.2.5"}], "ipv6": [{"address": "fe80::9002:c8ff:fee8:bb09", "prefix": "64", "scope": "link"}], "macaddress": "92:02:c8:e8:bb:09", "mtu": 1500, "promisc": False, "stp": False, "timestamping": ["rx_software", "software"], "type": "bridge"}, "ansible_effective_group_id": 900, "ansible_effective_user_id": 900, "ansible_enp0s3": {"active": True, "device": "enp0s3", "features": {"esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "fcoe_mtu": "off [fixed]", "generic_receive_offload": "on", "generic_segmentation_offload": "on", "highdma": "off [fixed]", "hw_tc_offload": "off [fixed]", "l2_fwd_offload": "off [fixed]", "large_receive_offload": "off [fixed]", "loopback": "off [fixed]", "netns_local": "off [fixed]", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "rx_all": "off", "rx_checksumming": "off", "rx_fcs": "off", "rx_gro_hw": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "rx_vlan_filter": "on [fixed]", "rx_vlan_offload": "on", "rx_vlan_stag_filter": "off [fixed]", "rx_vlan_stag_hw_parse": "off [fixed]", "scatter_gather": "on", "tcp_segmentation_offload": "on", "tls_hw_record": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_ip_generic": "on", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_sctp": "off [fixed]", "tx_checksumming": "on", "tx_esp_segmentation": "off [fixed]", "tx_fcoe_segmentation": "off [fixed]", "tx_gre_csum_segmentation": "off [fixed]", "tx_gre_segmentation": "off [fixed]", "tx_gso_partial": "off [fixed]", "tx_gso_robust": "off [fixed]", "tx_ipxip4_segmentation": "off [fixed]", "tx_ipxip6_segmentation": "off [fixed]", "tx_lockless": "off [fixed]", "tx_nocache_copy": "off", "tx_scatter_gather": "on", "tx_scatter_gather_fraglist": "off [fixed]", "tx_sctp_segmentation": "off [fixed]", "tx_tcp6_segmentation": "off [fixed]", "tx_tcp_ecn_segmentation": "off [fixed]", "tx_tcp_mangleid_segmentation": "off", "tx_tcp_segmentation": "on", "tx_udp_segmentation": "off [fixed]", "tx_udp_tnl_csum_segmentation": "off [fixed]", "tx_udp_tnl_segmentation": "off [fixed]", "tx_vlan_offload": "on [fixed]", "tx_vlan_stag_hw_insert": "off [fixed]", "vlan_challenged": "off [fixed]"}, "hw_timestamp_filters": [], "ipv4": {"address": "10.0.2.15", "broadcast": "10.0.2.255", "netmask": "255.255.255.0", "network": "10.0.2.0"}, "ipv6": [{"address": "fe80::a00:27ff:fee9:3de6", "prefix": "64", "scope": "link"}], "macaddress": "08:00:27:e9:3d:e6", "module": "e1000", "mtu": 1500, "pciid": "0000:00:03.0", "promisc": False, "speed": 1000, "timestamping": ["tx_software", "rx_software", "software"], "type": "ether"}, "ansible_env": {"DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/900/bus", "HOME": "/home/devasc", "LANG": "en_US.UTF-8", "LANGUAGE": "en_US:", "LOGNAME": "devasc", "MOTD_SHOWN": "pam", "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin", "PWD": "/home/devasc", "SHELL": "/bin/bash", "SHLVL": "0", "SSH_CLIENT": "192.0.2.3 55996 22", "SSH_CONNECTION": "192.0.2.3 55996 192.0.2.3 22", "SSH_TTY": "/dev/pts/3", "TERM": "xterm-256color", "USER": "devasc", "XDG_RUNTIME_DIR": "/run/user/900", "XDG_SESSION_CLASS": "user", "XDG_SESSION_ID": "96", "XDG_SESSION_TYPE": "tty", "_": "/bin/sh"}, "ansible_fibre_channel_wwn": [], "ansible_fips": False, "ansible_form_factor": "Other", "ansible_fqdn": "labvm.vm", "ansible_hostname": "labvm", "ansible_hostnqn": "", "ansible_interfaces": ["dummy0", "docker0", "lo", "vethacd0508", "enp0s3"], "ansible_is_chroot": False, "ansible_iscsi_iqn": "", "ansible_kernel": "5.4.0-37-generic", "ansible_kernel_version": "#41-Ubuntu SMP Wed Jun 3 18:57:02 UTC 2020", "ansible_lo": {"active": True, "device": "lo", "features": {"esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "fcoe_mtu": "off [fixed]", "generic_receive_offload": "on", "generic_segmentation_offload": "on", "highdma": "on [fixed]", "hw_tc_offload": "off [fixed]", "l2_fwd_offload": "off [fixed]", "large_receive_offload": "off [fixed]", "loopback": "on [fixed]", "netns_local": "on [fixed]", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "rx_all": "off [fixed]", "rx_checksumming": "on [fixed]", "rx_fcs": "off [fixed]", "rx_gro_hw": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "rx_vlan_filter": "off [fixed]", "rx_vlan_offload": "off [fixed]", "rx_vlan_stag_filter": "off [fixed]", "rx_vlan_stag_hw_parse": "off [fixed]", "scatter_gather": "on", "tcp_segmentation_offload": "on", "tls_hw_record": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_ip_generic": "on [fixed]", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_sctp": "on [fixed]", "tx_checksumming": "on", "tx_esp_segmentation": "off [fixed]", "tx_fcoe_segmentation": "off [fixed]", "tx_gre_csum_segmentation": "off [fixed]", "tx_gre_segmentation": "off [fixed]", "tx_gso_partial": "off [fixed]", "tx_gso_robust": "off [fixed]", "tx_ipxip4_segmentation": "off [fixed]", "tx_ipxip6_segmentation": "off [fixed]", "tx_lockless": "on [fixed]", "tx_nocache_copy": "off [fixed]", "tx_scatter_gather": "on [fixed]", "tx_scatter_gather_fraglist": "on [fixed]", "tx_sctp_segmentation": "on", "tx_tcp6_segmentation": "on", "tx_tcp_ecn_segmentation": "on", "tx_tcp_mangleid_segmentation": "on", "tx_tcp_segmentation": "on", "tx_udp_segmentation": "off [fixed]", "tx_udp_tnl_csum_segmentation": "off [fixed]", "tx_udp_tnl_segmentation": "off [fixed]", "tx_vlan_offload": "off [fixed]", "tx_vlan_stag_hw_insert": "off [fixed]", "vlan_challenged": "on [fixed]"}, "hw_timestamp_filters": [], "ipv4": {"address": "127.0.0.1", "broadcast": "host", "netmask": "255.0.0.0", "network": "127.0.0.0"}, "ipv6": [{"address": "::1", "prefix": "128", "scope": "host"}], "mtu": 65536, "promisc": False, "timestamping": ["tx_software", "rx_software", "software"], "type": "loopback"}, "ansible_local": {}, "ansible_lsb": {"codename": "focal", "description": "Ubuntu 20.04.1 LTS", "id": "Ubuntu", "major_release": "20", "release": "20.04"}, "ansible_machine": "x86_64", "ansible_machine_id": "c6a52afed8564edfa075a362c20348b8", "ansible_memfree_mb": 135, "ansible_memory_mb": {"nocache": {"free": 2292, "used": 1644}, "real": {"free": 135, "total": 3936, "used": 3801}, "swap": {"cached": 2, "free": 1927, "total": 2047, "used": 120}}, "ansible_memtotal_mb": 3936, "ansible_mounts": [{"block_available": 1933940, "block_size": 4096, "block_total": 7900888, "block_used": 5966948, "device": "/dev/sda5", "fstype": "ext4", "inode_available": 1581745, "inode_total": 2015232, "inode_used": 433487, "mount": "/", "options": "rw,relatime,errors=remount-ro", "size_available": 7921418240, "size_total": 32362037248, "uuid": "fb261367-cf98-4bce-b682-42b3de0a8ab9"}, {"block_available": 0, "block_size": 131072, "block_total": 783, "block_used": 783, "device": "/dev/loop6", "fstype": "squashfs", "inode_available": 0, "inode_total": 12867, "inode_used": 12867, "mount": "/snap/core/10444", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 102629376, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 747, "block_used": 747, "device": "/dev/loop8", "fstype": "squashfs", "inode_available": 0, "inode_total": 132, "inode_used": 132, "mount": "/snap/drawio/84", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 97910784, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 443, "block_used": 443, "device": "/dev/loop9", "fstype": "squashfs", "inode_available": 0, "inode_total": 10779, "inode_used": 10779, "mount": "/snap/core18/1932", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 58064896, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 1303, "block_used": 1303, "device": "/dev/loop10", "fstype": "squashfs", "inode_available": 0, "inode_total": 27807, "inode_used": 27807, "mount": "/snap/gnome-3-28-1804/145", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 170786816, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 519, "block_used": 519, "device": "/dev/loop12", "fstype": "squashfs", "inode_available": 0, "inode_total": 63978, "inode_used": 63978, "mount": "/snap/gtk-common-themes/1514", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 68026368, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 1404, "block_used": 1404, "device": "/dev/loop11", "fstype": "squashfs", "inode_available": 0, "inode_total": 44282, "inode_used": 44282, "mount": "/snap/postman/129", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 184025088, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 515, "block_used": 515, "device": "/dev/loop14", "fstype": "squashfs", "inode_available": 0, "inode_total": 63811, "inode_used": 63811, "mount": "/snap/gtk-common-themes/1513", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 67502080, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 1292, "block_used": 1292, "device": "/dev/loop15", "fstype": "squashfs", "inode_available": 0, "inode_total": 27798, "inode_used": 27798, "mount": "/snap/gnome-3-28-1804/128", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 169345024, "uuid": "N/A"}, {"block_available": 130811, "block_size": 4096, "block_total": 130812, "block_used": 1, "device": "/dev/sda1", "fstype": "vfat", "inode_available": 0, "inode_total": 0, "inode_used": 0, "mount": "/boot/efi", "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro", "size_available": 535801856, "size_total": 535805952, "uuid": "AF29-5078"}, {"block_available": 0, "block_size": 131072, "block_total": 1173, "block_used": 1173, "device": "/dev/loop2", "fstype": "squashfs", "inode_available": 0, "inode_total": 4207, "inode_used": 4207, "mount": "/snap/code/51", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 153747456, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 444, "block_used": 444, "device": "/dev/loop0", "fstype": "squashfs", "inode_available": 0, "inode_total": 10809, "inode_used": 10809, "mount": "/snap/core18/1944", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 58195968, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 784, "block_used": 784, "device": "/dev/loop17", "fstype": "squashfs", "inode_available": 0, "inode_total": 12867, "inode_used": 12867, "mount": "/snap/core/10583", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 102760448, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 1151, "block_used": 1151, "device": "/dev/loop4", "fstype": "squashfs", "inode_available": 0, "inode_total": 4207, "inode_used": 4207, "mount": "/snap/code/52", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 150863872, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 1403, "block_used": 1403, "device": "/dev/loop5", "fstype": "squashfs", "inode_available": 0, "inode_total": 42528, "inode_used": 42528, "mount": "/snap/postman/130", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 183894016, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 948, "block_used": 948, "device": "/dev/loop13", "fstype": "squashfs", "inode_available": 0, "inode_total": 1330, "inode_used": 1330, "mount": "/snap/chromium/1444", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 124256256, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 740, "block_used": 740, "device": "/dev/loop18", "fstype": "squashfs", "inode_available": 0, "inode_total": 132, "inode_used": 132, "mount": "/snap/drawio/99", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 96993280, "uuid": "N/A"}, {"block_available": 0, "block_size": 131072, "block_total": 1086, "block_used": 1086, "device": "/dev/loop7", "fstype": "squashfs", "inode_available": 0, "inode_total": 1355, "inode_used": 1355, "mount": "/snap/chromium/1466", "options": "ro,nodev,relatime", "size_available": 0, "size_total": 142344192, "uuid": "N/A"}], "ansible_nodename": "labvm", "ansible_os_family": "Debian", "ansible_pkg_mgr": "apt", "ansible_proc_cmdline": {"BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic", "quiet": True, "ro": True, "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9", "vga": "792", "zswap.enabled": "1"}, "ansible_processor": ["0", "GenuineIntel", "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz", "1", "GenuineIntel", "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz"], "ansible_processor_cores": 2, "ansible_processor_count": 1, "ansible_processor_threads_per_core": 1, "ansible_processor_vcpus": 2, "ansible_product_name": "VirtualBox", "ansible_product_serial": "NA", "ansible_product_uuid": "NA", "ansible_product_version": "1.2", "ansible_python": {"executable": "/usr/bin/python3", "has_sslcontext": True, "type": "cpython", "version": {"major": 3, "micro": 2, "minor": 8, "releaselevel": "final", "serial": 0}, "version_info": [3, 8, 2, "final", 0]}, "ansible_python_version": "3.8.2", "ansible_real_group_id": 900, "ansible_real_user_id": 900, "ansible_selinux": {"status": "disabled"}, "ansible_selinux_python_present": True, "ansible_service_mgr": "systemd", "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPFM1OVBLhbMfZVSkIVrPTq0FcKqNM9vRuBawNKkevM0UoDO5PwzaDCS6Hry9lvKuJIP+aB5KNnQ0P6uZfHdpFc=", "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIC5pTSLWhV+w/qgqcGewKBfdDczo4VhV3VWp1lLHH7U+", "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQCpwiwXYyl8eNmZO2dfWYyV1V1pnoq/tZjXF9ABBSSsR7KHny7SP4muQvLErLc2wOlvzsYq5l/NQoYuIeY7eGK3dffACUwda9V1Ub6AjcNQIdwLypUt1zW3Q/9e8/VfnmVGr5IeIvt02L362V4jFfLYd8QZxqlzWO7ah8bODyvGP68VP6pE7Hd+XamJAwMHH0NquCeRW5JO6xWaTVvZUiNGVYSTl0OFDuXX/CbXVXMjaaPF1ZJuLtpmfxAcmtIKRqHUmy0wWRah3GXiLwpAR4i50jlgE84Y1swqEpMneAM/nanFwrCEMBmf54olazJ1e3redxIyWFCDwhZO+Q0sZoruS3OXfpsr9/33uksfjP4TiQHy84Xn5WhR/VRRsCyqA7adn/4FmtUtbOR0eaD3pBPGElocCSy7p/wOO18B6Bfa0BSoh8si+ShBNxNVuULw2/iCebRbReXaw9xbfNFx5bJVSfJmZfJvRVpQV9HVZYV2apKuHyFbwLROAf0NRwAJxm8=", "ansible_swapfree_mb": 1927, "ansible_swaptotal_mb": 2047, "ansible_system": "Linux", "ansible_system_capabilities": [""], "ansible_system_capabilities_enforced": "True", "ansible_system_vendor": "innotek GmbH", "ansible_uptime_seconds": 158482, "ansible_user_dir": "/home/devasc", "ansible_user_gecos": "DevNet Associate,,,", "ansible_user_gid": 900, "ansible_user_id": "devasc", "ansible_user_shell": "/bin/bash", "ansible_user_uid": 900, "ansible_userspace_architecture": "x86_64", "ansible_userspace_bits": "64", "ansible_vethacd0508": {"active": True, "device": "vethacd0508", "features": {"esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "fcoe_mtu": "off [fixed]", "generic_receive_offload": "on", "generic_segmentation_offload": "on", "highdma": "on", "hw_tc_offload": "off [fixed]", "l2_fwd_offload": "off [fixed]", "large_receive_offload": "off [fixed]", "loopback": "off [fixed]", "netns_local": "off [fixed]", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "rx_all": "off [fixed]", "rx_checksumming": "on", "rx_fcs": "off [fixed]", "rx_gro_hw": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "rx_vlan_filter": "off [fixed]", "rx_vlan_offload": "on", "rx_vlan_stag_filter": "off [fixed]", "rx_vlan_stag_hw_parse": "on", "scatter_gather": "on", "tcp_segmentation_offload": "on", "tls_hw_record": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_ip_generic": "on", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_sctp": "on", "tx_checksumming": "on", "tx_esp_segmentation": "off [fixed]", "tx_fcoe_segmentation": "off [fixed]", "tx_gre_csum_segmentation": "on", "tx_gre_segmentation": "on", "tx_gso_partial": "off [fixed]", "tx_gso_robust": "off [fixed]", "tx_ipxip4_segmentation": "on", "tx_ipxip6_segmentation": "on", "tx_lockless": "on [fixed]", "tx_nocache_copy": "off", "tx_scatter_gather": "on", "tx_scatter_gather_fraglist": "on", "tx_sctp_segmentation": "on", "tx_tcp6_segmentation": "on", "tx_tcp_ecn_segmentation": "on", "tx_tcp_mangleid_segmentation": "on", "tx_tcp_segmentation": "on", "tx_udp_segmentation": "off [fixed]", "tx_udp_tnl_csum_segmentation": "on", "tx_udp_tnl_segmentation": "on", "tx_vlan_offload": "on", "tx_vlan_stag_hw_insert": "on", "vlan_challenged": "off [fixed]"}, "hw_timestamp_filters": [], "ipv6": [{"address": "fe80::3c67:a5ff:fe17:e4cf", "prefix": "64", "scope": "link"}], "macaddress": "3e:67:a5:17:e4:cf", "mtu": 1500, "promisc": True, "speed": 10000, "timestamping": ["tx_software", "rx_software", "software"], "type": "ether"}, "ansible_virtualization_role": "guest", "ansible_virtualization_type": "virtualbox", "discovered_interpreter_python": "/usr/bin/python3", "gather_subset": ["all"], "module_setup": True}, "changed": False, "deprecations": [], "warnings": []}
print(resp.keys())
#print(resp["ansible_facts"].keys())
print("Ansible First IPv4 Address: "    + resp["ansible_facts"]["ansible_all_ipv4_addresses"][0])
print("Ansible Distribution: "          + resp["ansible_facts"]["ansible_distribution"])
print("Ansible Distribution Release: "  + resp["ansible_facts"]["ansible_distribution_release"])
print("Ansible Distribution Version: "  + resp["ansible_facts"]["ansible_distribution_version"])


# In[2]:


### 10 ###
### Needed: external file created by Ansible
### Ansible Response Data --- very long --------------------------------------
### External file can be downloaded here: https://docs.google.com/document/d/1Z7wO5r8XaBirxXo06CmC8a6r5cCMezQQqUOcHxXhCyk/edit?usp=sharing
### $ ansible webservers -m gather_facts --tree ./tmp_facts
"""
ANSIBLE PARSE OUTPUT 
FILE: ansible_gather_facts.json
"""
with open('ansible_gather_facts.json', 'r') as file:
    #ansible_json_doc = file.read().replace('\n', '')
    ansible_json_doc = file.read()
print("DATA FROM FILE: " + ansible_json_doc)


# In[2]:


### 11 ###
### RUN PREVIOUS CELL FIRST
import json
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
ansible_dict = json.loads(ansible_json_doc)
print(ansible_dict.keys())
print("---------2--------")
print("Converting dict to raw json")
ansible_json = json.dumps(ansible_dict)
print(ansible_json)


# In[3]:


### 12 ###
### RUN PREVIOUS CELL FIRST
# PARSING AND FILTERING ANSIBLE JSON DATA 
print("---------1--------")
print("Showing dictionary keys at level 1")
#ansible_dict = json.loads(ansible_json_doc)
print(ansible_dict.keys())
print("---------2--------")
print("Showing keys of ansible facts at level 2")
print(ansible_dict['ansible_facts'].keys())
print("---------3--------")
print("Showing data below ansible facts: ip address")
print("IP Address: " + ansible_dict["ansible_facts"]["ansible_default_ipv4"]["address"])
print('---------4--------')
print("Showing data below ansible facts: ansible distribution")
print("Ansible Distribution: "  + ansible_dict["ansible_facts"]["ansible_distribution"])
print("Ansible Distribution Major: "  + ansible_dict["ansible_facts"]["ansible_distribution_major_version"])
print("Ansible Distribution Release: "  + ansible_dict["ansible_facts"]["ansible_distribution_release"])
print("Ansible Distribution Version: "  + ansible_dict["ansible_facts"]["ansible_distribution_version"])
print('---------5--------')
print("Showing data below ansible facts: kernel, nodename, os")
print("Ansible Kernel: "  + ansible_dict["ansible_facts"]["ansible_kernel"])
print("Ansible Nodename: "     + ansible_dict["ansible_facts"]["ansible_nodename"])
print("Ansible OS Family: "    + ansible_dict["ansible_facts"]["ansible_os_family"])
print("Ansible PKG Manager: "  + ansible_dict["ansible_facts"]["ansible_pkg_mgr"])
print("Ansible Python Version: "  + ansible_dict["ansible_facts"]["ansible_python_version"])
print('---------6--------')
print("Showing data below ansible facts: ansible environment")
print("Ansible Home: "  + ansible_dict["ansible_facts"]["ansible_env"]["HOME"])
print("Ansible User: "  + ansible_dict["ansible_facts"]["ansible_env"]["USER"])


# In[38]:


### 13 ###
### Needed: external file created by docker 
### Docker Response Data -- docker image (partial)
### You can download the file here: https://drive.google.com/file/d/1DM641DhTuJ7FxbZJEGqIR8dhYPLEGaoX/view?usp=sharing
"""
DOCKER  PARSE OUTPUT -- 1 
FILE: docker_image_inspect_ubunt.txt
"""
with open('docker_image_inspect_ubunt.txt', 'r') as file:
    docker_json_file = file.read()
print("JSON DATA FROM FILE: " + docker_json_file)


# In[39]:


### 14 ###
### RUN PREVIOUS CELL FIRST => READ EXTERNAL FILE GENEREATED BY DOCKER
import json
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict = json.loads(docker_json_file)
print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print(docker_json)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])


# In[40]:


### 15 ###
### Docker Response Data -- docker network (partial)
### Needed: external file created by docker 
### You can download the file here: https://drive.google.com/file/d/15oHKwKaFdTXx62GjhY6cvCUuNyx-cWhu/view?usp=sharing
"""
DOCKER  PARSE OUTPUT -- 2
FILE: docker_inspect_network.txt
"""
with open('docker_inspect_network.txt', 'r') as file:
    docker_json_file2 = file.read()
print("DATA FROM FILE: " + docker_json_file2)


# In[41]:


### 16 ###
### RUN PREVIOUS CELL FIRST => READ EXTERNAL FILE GENEREATED BY DOCKER
import json
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict2 = json.loads(docker_json_file2)
print(docker_dict2[0].keys())
print("Converting json string to dict, and showing keys at level 2-3")
print(docker_dict2[0]["Containers"].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.dumps(docker_dict2)
print("Filtering from dict")
print(docker_dict2[0]["Name"])
print(docker_dict2[0]["Created"])
print(docker_dict2[0]["Containers"]["4e99a64e10dfcf6608a1d47f4349676c745bf234cebd52826d786db9a3be2811"]["IPv4Address"])


# In[25]:


### 17 ###
### Webex Groups Dict Example
### Simplified code: Read two records

groups_struc = {
 "groups": [
      { "group": { "group_id": "G-A" 
                 , "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Nick", "email": "nick@odisee.be"},
                     {"person_id": "P-2" , "person_name": "Mary", "email": "mary@odisee.be"},
                     {"person_id": "P-3" , "person_name": "Jens", "email": "jens@odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G-B" 
                 , "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Ives", "email": "ives@odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "John", "email": "john@odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Alec", "email": "alec@odisee.be"} 
                   ]     
                 }
      } 
   ]
}

### Select first group, first person
resp_a1 = groups_struc["groups"][0]["group"]["group_name"]
resp_a2 = groups_struc["groups"][0]["group"]["members"][0]["person_name"]

### Select second group; first person
resp_b1 = groups_struc["groups"][1]["group"]["group_name"]
resp_b2 = groups_struc["groups"][1]["group"]["members"][0]["person_name"]

print("First group, First person")
print(resp_a1 + " => " + resp_a2)

print("Second group, First person")
print(resp_b1 + " => " + resp_b2)


# In[26]:


### 18 ###
### Webex Groups Dict Example - 2
### Loop to select all groups and members

groups_struc = {
 "groups": [
      { "group": { "group_id": "G-A" 
                 , "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Nick", "email": "nick@odisee.be"},
                     {"person_id": "P-2" , "person_name": "Mary", "email": "mary@odisee.be"},
                     {"person_id": "P-3" , "person_name": "Jens", "email": "jens@odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G-B" 
                 , "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Ives", "email": "ives@odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "John", "email": "john@odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Alec", "email": "alec@odisee.be"} 
                   ]     
                 }
      } 
   ]
}

### All groups with members and email addresses
for g in groups_struc["groups"]:
    print(g["group"]["group_name"])
    for p in g["group"]["members"]:
        print(p["person_name"] + " => " + p["email"])


# In[44]:


### 19 ###
### - Network Devices Dict Example
### Loop to select all network devices and interfaces
rack_struc = {
 "rack": [
      { "device": { "dev_id": "D1" , 
                    "dev_name": "R1" , 
                    "role": "router"  ,      
                    "interfaces": [   
                      {"interface": "GigabitEthernet1" , 
                       "ipaddress": "10.0.1.1", 
                       "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEthernet2" , 
                       "ipaddress": "10.0.3.1", 
                       "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEthernet3" , 
                       "ipaddress": "10.0.4.1", 
                       "subnet_mask": "255.255.255.0"} 
                     ]
                 }
      } 
   ]
}

### All network devices interfaces and ip addresses
for g in rack_struc["rack"]:
    print(g["device"]["dev_name"])
    for p in g["device"]["interfaces"]:
        print(p["interface"]+" => "+p["ipaddress"])


# In[25]:


### 20 ### Newly added data structure
### Subnetting Dict Example - Class C network divided in 4 subnets
### Example
subnet_struc = {
    "subnets": [{
            "subnet": {
                "subnet_number": "0",
                "subnet_address": "192.168.0.0",
                "first_host": "192.168.0.1",
                "last_host": "192.168.0.62",
                "broadcast_address": "192.168.0.63"
            }
        },
        {
            "subnet": {
                "subnet_number": "1",
                "subnet_address": "192.168.0.64",
                "first_host": "192.168.0.65",
                "last_host": "192.168.0.126",
                "broadcast_address": "192.168.0.127"
            }
        },
        {
            "subnet": {
                "subnet_number": "2",
                "subnet_address": "192.168.0.128",
                "first_host": "192.168.0.129",
                "last_host": "192.168.0.190",
                "broadcast_address": "192.168.0.191"
            }
        },
        {
            "subnet": {
                "subnet_number": "3",
                "subnet_address": "192.168.0.192",
                "first_host": "192.168.0.193",
                "last_host": "192.168.0.254",
                "broadcast_address": "192.168.0.255"
            }
        }
        ]
}

print(type(subnet_struc))
#print(subnet_struc)
###
### select information about a specific subnet
selected_subnet = 0 
print(subnet_struc["subnets"][selected_subnet]["subnet"]["subnet_number"])
print(subnet_struc["subnets"][selected_subnet]["subnet"]["subnet_address"])
print(subnet_struc["subnets"][selected_subnet]["subnet"]["first_host"])
print(subnet_struc["subnets"][selected_subnet]["subnet"]["last_host"])
print(subnet_struc["subnets"][selected_subnet]["subnet"]["broadcast_address"])
###
### loop through all subnets
for n in subnet_struc["subnets"]:
    print(n["subnet"]["subnet_number"] 
          + " => " + n["subnet"]["subnet_address"]
          + " => " + n["subnet"]["first_host"]
          + " => " + n["subnet"]["last_host"]
          + " => " + n["subnet"]["broadcast_address"]
         )
    


# In[12]:


### 21 ### Newly added: Googel Geolocation response data 
### Response data from Google Geolocation
import json
resp = {'results': [{'address_components': [{'long_name': 'Halle', 'short_name': 'Halle', 'types': ['locality', 'political']}, {'long_name': 'Flemish Brabant', 'short_name': 'VB', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Flanders', 'short_name': 'Flanders', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Belgium', 'short_name': 'BE', 'types': ['country', 'political']}], 'formatted_address': 'Halle, Belgium', 'geometry': {'bounds': {'northeast': {'lat': 50.7785199, 'lng': 4.31185}, 'southwest': {'lat': 50.68936, 'lng': 4.17231}}, 'location': {'lat': 50.73757, 'lng': 4.23251}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 50.7785199, 'lng': 4.31185}, 'southwest': {'lat': 50.68936, 'lng': 4.17231}}}, 'place_id': 'ChIJR3tSDfjIw0cR6DrZHBsfLcE', 'types': ['locality', 'political']}], 'status': 'OK'}
print("------1--------")
print(type(resp))
print("------2--------")
json_data = json.dumps(resp, indent=2)
print(type(json_data))
print("------3--------")
print(json_data)


# In[13]:


### 22 ### Newly added: Googel Geolocation response data 
### Response data from Google Geolocation
import json
resp = {'results': [{'address_components': [{'long_name': 'Namur', 'short_name': 'Namur', 'types': ['locality', 'political']}, {'long_name': 'Province of Namur', 'short_name': 'NA', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Wallonia', 'short_name': 'Wallonia', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Belgium', 'short_name': 'BE', 'types': ['country', 'political']}], 'formatted_address': 'Namur, Belgium', 'geometry': {'bounds': {'northeast': {'lat': 50.5312201, 'lng': 4.98398}, 'southwest': {'lat': 50.38738, 'lng': 4.7229}}, 'location': {'lat': 50.4673883, 'lng': 4.8719854}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 50.5312201, 'lng': 4.98398}, 'southwest': {'lat': 50.38738, 'lng': 4.7229}}}, 'place_id': 'ChIJP2UsDG2ZwUcRBVIWxLYmVsE', 'types': ['locality', 'political']}, {'address_components': [{'long_name': 'Province of Namur', 'short_name': 'NA', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Wallonia', 'short_name': 'Wallonia', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Belgium', 'short_name': 'BE', 'types': ['country', 'political']}], 'formatted_address': 'Province of Namur, Belgium', 'geometry': {'bounds': {'northeast': {'lat': 50.64833, 'lng': 5.4025}, 'southwest': {'lat': 49.78548000000001, 'lng': 4.28589}}, 'location': {'lat': 50.3310218, 'lng': 4.8221456}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 50.64833, 'lng': 5.4025}, 'southwest': {'lat': 49.78548000000001, 'lng': 4.28589}}}, 'place_id': 'ChIJGVmGENGUwUcRorXKNtkQZS0', 'types': ['administrative_area_level_2', 'political']}], 'status': 'OK'}
print("------1--------")
print(type(resp))
print("------2--------")
json_data = json.dumps(resp, indent=2)
print(type(json_data))
print("------3--------")
print(json_data)

