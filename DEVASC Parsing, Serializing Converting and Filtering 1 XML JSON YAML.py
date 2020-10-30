#!/usr/bin/env python
# coding: utf-8

# In[23]:

#### DEVASC Parsing, Converting, Filtering
#### XML, JSON, YAML
#### Y. Rooseleer, BIASC, 2020
#### XML Parsing and Regular Expressions -- difficult, prefer xmltodict
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML Parsing')
import xml.etree.ElementTree as ET
import re
doc =   """
        <?xml version="1.0" encoding="UTF-8"?>
        <rpc message-id="1"
         xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <edit-config>
        <target>
           <candidate/>
        </target>
        <default-operation>merge</default-operation>
        <test-option>set</test-option>
        <config>
           <int8.1
            xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"
            nc:operation="create"
            xmlns="http://netconfcentral.org/ns/test">9</int8.1>
        </config>
        </edit-config>
        </rpc>
    """
print(doc)
####
print('-----1-----')
xml_in = ET.parse("netconf_file.xml")
print("Showing XML root data read from external file")
print(xml_in)
root = xml_in.getroot()
print(root.tag)
print("XML namespace")
#### Below <.*> => match an entire string
####‼ group() Return the string matched by the RE
ns = re.match('{.*}', root.tag).group(0)
print(ns)
print(type(ns))
#### print(dir(root))
####for it in root.iter():
####    print(it)
print('-----2------')
print("Showing XML keys parsed")
nc_data = root.keys()
print(nc_data)
#### Below: {} is a placeholder for Python string formatting
editconf = root.find("{}edit-config".format(ns))
#print(type(editconf))
#print(dir(editconf))
for it in editconf.iter():
    print(type(it))
    print(it)
print('-----3------')
print("Extracting netconf operations")
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))
print(defop.text)
print(testop.text)


# In[24]:


### XML Parsing into json => easier than xml.etree above
###!pip install xmltodict
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import json
import xmltodict
#### delete line from XML file: <?xml version="1.0" encoding="UTF-8"?>
doc = xmltodict.parse(
    """
        <rpc message-id="1"
         xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <edit-config>
        <target>
           <candidate/>
        </target>
        <default-operation>merge</default-operation>
        <test-option>set</test-option>
        <config>
           <int8.1
            xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"
            nc:operation="create"
            xmlns="http://netconfcentral.org/ns/test">9</int8.1>
        </config>
        </edit-config>
        </rpc>
    """
)
#print('----SHOW RAW DICT/JSON----')
#print('RAW - serialized - string')
#print(doc)
#print('----SHOW DICT/JSON----')
#print('Prettified')
print(json.dumps(doc, indent=4))
#### Converting to str, and to json
str_doc = json.dumps(doc, indent=4)
json_doc = json.loads(str_doc)
####
print('----SHOW DATA TYPES----')
print(type(doc))
print(type(str_doc))
print(type(json_doc))
print('----SHOW STRUCTURE----')
print(json_doc.keys())
print(json_doc["rpc"].keys())
print(json_doc["rpc"]["edit-config"].keys())
print(json_doc["rpc"]["edit-config"]["config"].keys())
print(json_doc["rpc"]["edit-config"]["config"]["int8.1"].keys())
print('----SHOW OPERATIONS----')
print(json_doc["rpc"]["@message-id"])
print(json_doc["rpc"]["edit-config"]["default-operation"])
print(json_doc["rpc"]["edit-config"]["test-option"])
print(json_doc["rpc"]["edit-config"]["config"]["int8.1"]["@nc:operation"])


# In[26]:


import json
atk = {
 "access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
 "expires_in":1209600,
 "refresh_token":"MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4",
 "refreshtokenexpires_in":7776000
}
print('-----1-----')
print (type(atk))
print(atk)
#### pretty output
print('-----2-----')
print(json.dumps(atk, indent=2))
#### FILTERING DATA
#### filter access-token
print('-----3-----')
print(atk["access_token"])
#### TRANSFORMING DATA TYPES
print('-----4-----')
ats = json.dumps(atk)
print(type(ats))
####
print('-----5-----')
atj = json.loads(ats)
print(type(atj))


# In[8]:


import json
import yaml
doc = """
---
access_token: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
expires_in: 1209600
refresh_token: MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4
refreshtokenexpires_in: 7776000
"""
print(type(doc))
print(doc)
#The function yaml.load converts a YAML document to a Python object.
#Warning: It is not safe to call yaml.load with any data received from an untrusted source, therefore "safe_load"
###The yaml.dump function accepts a Python object and produces a YAML document.
acc = yaml.safe_load(doc)
print('------------')
print (type(acc))
print('------------')
print(acc)
at = acc['access_token']
print('------------')
print(at)


# In[9]:


#JSON YAML
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- converting json to yaml')
import json
import yaml
########
print("------1------")
json_data = """
{
  "Cisco-IOS-XE-native:GigabitEthernet": {
    "name": "1",
    "vrf": {
      "forwarding": "MANAGEMENT"
    },
    "ip": {
      "address": {
        "primary": {
          "address": "10.0.0.151",
          "mask": "255.255.255.0"
        }
      }
    },
    "mop": {
      "enabled": false
    },
    "Cisco-IOS-XE-ethernet:negotiation": {
      "auto": true
    }
  }
}
"""
print("Showing json_data format")
print(type(json_data))
#print(json_data)
print("------2------")
print("Showing json_data in raw format")
json_dict = json.loads(json_data)
print(type(json_dict))
print(json_dict)
print("------3------")
print("Showing json_data indented")
print(json.dumps(json_dict, indent=4))
print("------4------")
print("Showing filtered data: primary IP Adddress")
print(json_dict["Cisco-IOS-XE-native:GigabitEthernet"]["ip"]["address"]["primary"]["address"])
print("------5------")
print("Showing filtered data: interface status")
#print(json_dict["Cisco-IOS-XE-native:GigabitEthernet"]["mop"]["enabled"])
if json_dict["Cisco-IOS-XE-native:GigabitEthernet"]["mop"]["enabled"]:
    print("Interface enabled")
else:
    print("Interface shutdown")
print("------6-----")
# Converting to YAML
print("Converting to YAML format")
#The yaml.dump function accepts a Python object and produces a YAML document.
yaml_data = yaml.dump(json_dict)
print("Internal format of converted data")
print(type(yaml_data))
print("\n---")
print("Data formatted in YAML output")
print(yaml_data)


# In[10]:


###XML
###!pip install xmltodict
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
doc = xmltodict.parse(
    """
    <GigabitEthernet>
      <name>1</name>
      <vrf>
        <forwarding>MANAGEMENT</forwarding>
      </vrf>
      <ip>
        <address>
           <primary>
              <address>10.0.0.151</address>
              <mask>255.255.255.0</mask>
           </primary>
        </address>
      </ip>
      <mop>
        <enabled>false</enabled>
      </mop>
      <negotiation>
        <auto>true</auto>
      </negotiation>
    </GigabitEthernet>
    """
)
print('------1------')
print('RAW - serialized - string')
print(doc)
print(type(doc))
print('------2------')
print('Prettified')
print(json.dumps(doc, indent=8))
print('------3------')
print('Filtering')
filtered_item  = doc["GigabitEthernet"]["ip"]["address"]["primary"]["address"]
print(filtered_item)
filtered_item  = doc["GigabitEthernet"]["ip"]["address"]["primary"]["mask"]
print(filtered_item)


# In[11]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
doc = xmltodict.parse(
    """
        <vms>
          <vm>
            <vmid>1--0101af9811012</vmid>
            <type>t1.nano</type>
          </vm>
           <vm>
            <vmid>2--0102bg89087023</vmid>
            <type>t1.micro  </type>
          </vm>
        </vms>
    """
)
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[12]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
doc = xmltodict.parse(
    """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"  xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>GigabitEthernet1</name>
    <description>VBox</description>
    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
    <enabled>true</enabled>
    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
    </ipv4>
    <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
    </ipv6>
  </interface>
  <interface>
    <name>Loopback9</name>
    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
    <enabled>true</enabled>
    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
      <address>
        <ip>10.0.0.9</ip>
        <netmask>255.255.255.0</netmask>
      </address>
    </ipv4>
    <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
    </ipv6>
  </interface>
</interfaces>
"""
)
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[13]:


#netconf
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
########
doc = xmltodict.parse(
    """
    <data>
        <interfaces>
            <interface>
                <name>GigabitEthernet1</name>
                <description>Management interface</description>
                <type>ianaift:ethernetCsmacd</type>
                <enabled>true</enabled>
                <ipv4>
                    <address>
                        <ip>10.10.20.48</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
                <ipv6/>
            </interface>  
        </interfaces>
    </data>
"""
)
######## 
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[14]:


#netconf
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
########
doc = xmltodict.parse(
    """
    <data>
        <interfaces>
            <interface>
                <name>GigabitEthernet1</name>
                <description>Management interface</description>
                <type>ianaift:ethernetCsmacd</type>
                <enabled>true</enabled>
                <ipv4>
                    <address>
                        <ip>10.10.20.48</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
                <ipv6/>
            </interface>  
            <interface>
                <name>GigabitEthernet2</name>
                <description>Voice interface</description>
                <type>ianaift:ethernetCsmacd</type>
                <enabled>true</enabled>
                <ipv4>
                    <address>
                        <ip>10.10.20.49</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
                <ipv6/>
            </interface>  
        </interfaces>
    </data>
"""
)
######## 
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[15]:


#APIs
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
########
doc = xmltodict.parse(
    """
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>198.18.133.212</ip>
                    <netmask>255.255.192.0</netmask>
                </address>
            </ipv4>
            <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        </interface>
    </interfaces>
"""
)
########
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[16]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
########
doc = xmltodict.parse(
    """
    <server>
      <pool>http</pool>
      <desciption>MY vst</desciption>
      <name>http-virtual</name>
      <mask>255.255.255.255</mask>
      <profiles>
        <name>http</name>
        <kind>l:v:m</kind>
      </profiles>
      <profiles>
        <name>tcp</name>
        <kind>l:v:m</kind>
      </profiles>
      <ipprotocol>>tcp</ipprotocol>>
      <sourceaddresstanslation>automap</sourceaddresstanslation>
      <kind>t:l:v:v</kind>
      <destination>1.1.1.3:80 </destination>
    </server>
"""
)
########
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[17]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML PARSING')
import xmltodict
########
data_d = xmltodict.parse(
    """
       <vms>
         <vm>
            <vmid>0101af9811012</vmid>
            <type>t1.nano</type>
         </vm>
         <vm>
            <vmid>0102bg8908023</vmid>
            <type>t1.micro</type>
         </vm>
      </vms>
"""
)
########
print('----------------')
print('RAW - serialized - string')
print(data_d)
print('----------------')
print('Prettified')
print(json.dumps(data_d, indent=2))


# In[18]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML PARSING')
import xmltodict
########
data_d = xmltodict.parse("""<device><Hostname>Lin01</Hostname><IPv4>10.10.133.1</IPv4><IPv6> </IPv6></device>""")
########
print('----------------')
print('RAW - serialized - string')
print(data_d)
print('----------------')
print('Prettified')
print(json.dumps(data_d, indent=2))


# In[19]:


#### DICT => JSON => YAML
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
import json
import yaml
from tabulate import tabulate
print('Starting dict, filtering, formating, converting ...')
####
userlist = {           
  "users": [
      {"username": "GHI","code": "GHI123951" },
      {"username": "ABC","code": "ABC123951" },
      {"username": "DEF","code": "DEF123951" },
      {"username": "JKL","code": "JKL123951" },
      {"username": "MNO","code": "MNO123951" },
   ]
}
print("\n------1------")
print("Showing userlist in raw format")
print(type(userlist))
print(userlist)
####print(userlist["users"])
print("Printing users in table format")
print(tabulate(userlist["users"]))
print("------2------")
print("Showing users using filter")
print(userlist["users"][0]["username"])
print(userlist["users"][1]["username"])
print(userlist["users"][-1]["username"])
print(userlist["users"][-2]["username"])
print("------3------")
print("Showing userlist using loop")
for usr in userlist["users"]:
    print(usr["username"])
print("------4-----")
print("Showing dict in indented JSON format")
userlist_out = json.dumps(userlist, indent=8)
print(type(userlist_out))
print(userlist_out)
print("------5-----")
print("Showing dict in YAML format")
userlist_yaml = yaml.dump(userlist)
print(type(userlist_yaml))
print("\n---")
print(userlist_yaml)
#######################
#### JSON is a serialization format
#### That is, JSON is a way of representing structured data in the form of a textual string.
#### DICT (dictionary) is a data structure. That is, it is a way of storing data in memory 
#### that provides certain abilities to your code: in the case of dictionaries, 
#### those abilities include rapid lookup and enumeration.


# In[20]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import xmltodict
import json
########
doc = xmltodict.parse(
    """
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>
"""
)
########
print('----------------')
print('RAW - serialized - string')
print(doc)
print('----------------')
print('Prettified')
print(json.dumps(doc, indent=2))


# In[21]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML PARSING')
import xml.etree.ElementTree as ET
########
data_c = """
        <data>
            <country name="Liechtenstein">
                <rank>1</rank>
                <year>2008</year>
                <gdppc>141100</gdppc>
                <neighbor name="Austria" direction="E"/>
                <neighbor name="Switzerland" direction="W"/>
            </country>
            <country name="Singapore">
                <rank>4</rank>
                <year>2011</year>
                <gdppc>59900</gdppc>
                <neighbor name="Malaysia" direction="N"/>
            </country>
            <country name="Panama">
                <rank>68</rank>
                <year>2011</year>
                <gdppc>13600</gdppc>
                <neighbor name="Costa Rica" direction="W"/>
                <neighbor name="Colombia" direction="E"/>
            </country>
        </data>
"""
########
#tree = ET.parse("filename")
#dir(ET)
root = ET.fromstring(data_c)
print(type(root))
for child in root:
    print(child.tag, child.attrib)
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)


# In[22]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML PARSING')
import xml.etree.ElementTree as ET
########
data_a = """
        <actors xmlns:fictional="http://characters.example.com"
            xmlns="http://people.example.com">
          <actor>
              <name>John Cleese</name>
              <fictional:character>Lancelot</fictional:character>
              <fictional:character>Archie Leach</fictional:character>
          </actor>
          <actor>
              <name>Eric Idle</name>
              <fictional:character>Sir Robin</fictional:character>
              <fictional:character>Gunther</fictional:character>
              <fictional:character>Commander Clement</fictional:character>
          </actor>
        </actors>
"""
########
#tree = ET.parse("filename")
#dir(ET)
root = ET.fromstring(data_a)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)


# In[ ]:


#JSON
import json
import yaml
########
json_data = """
            {"Cisco-IOS-XE-native:GigabitEthernet": {"name": "1",
             "vrf": {"forwarding": "MANAGEMENT"},
             "ip": {"address": {"primary": {"address": "10.0.0.151","mask": "255.255.255.0"}}},
             "mop": {"enabled": false},"Cisco-IOS-XE-ethernet:negotiation": {"auto": true}}}
"""
########
print(type(json_data))
print(json_data)
json_dict = json.loads(json_data)
print(type(json_dict))
print("============")
print(json_dict)
print("============")
print(json.dumps(json_dict, indent=2))
print("============")
print(json_dict["Cisco-IOS-XE-native:GigabitEthernet"]["ip"]["address"]["primary"]["address"])
print("============")
#print(json_dict["Cisco-IOS-XE-native:GigabitEthernet"]["mop"]["enabled"])
if json_dict["Cisco-IOS-XE-native:GigabitEthernet"]["mop"]["enabled"]:
    print("Interface enabled")
else:
    print("Interface shutdown")
print("============")
#CONVERTING JSON TO YAML
print("Concverting JSON to YAML")
print("\n\n---")
print(yaml.dump(json_dict))


# In[ ]:


#### XML Parsing and Regular Expressions -- config example
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML Parsing')
import xml.etree.ElementTree as ET
import re
print('-----1-----')
xml = ET.parse("netconf_file2.xml")
print(xml)
root = xml.getroot()
print(root.tag)
print(root.keys())
print('-----2-----')
### Below <.*> => match an entire string
ns = re.match('{.*}', root.tag).group(0)
print(ns)
print(type(ns))
print('-----3------')
####print(dir(root))
for it in root.iter():
    print(it)
#### Below: {} is a placeholder for Python string formatting
#editconf = root.find("{}edit-config".format(ns))
#defop = editconf.find("{}default-operation".format(ns))
#testop = editconf.find("{}test-option".format(ns))
#print(defop.text)
#print(testop.text)


# In[ ]:


#!pip install dicttoxml
import dicttoxml   
import requests    
auth = {           
  "user": {
    "username": "myemail@mydomain.com",
    "key": "90823ff08409408aebcf4320384"
  }
}
print("------1------")
print(type(auth))
print("------2------")
print(auth)
print("------3------")
print(auth["user"]["username"])
print("----------------")
#get_services_query = "https://myservice.com/status/services"
####xmlstring = dicttoxml(auth)     
#myresponse = requests.get(get_services_query,auth=xmlstring)  
###print(xmlstring)


# In[ ]:


# TO BE UPDATED
########
import json
import yaml
yaml_data = """
            ---
            access_token: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
            expires_in: 1209600
            refresh_token: MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4
            refreshtokenexpires_in: 7776000
"""
########
print("------1------")
print(type(yaml_data))
print(yaml_data)
#python_data = yaml.safe_load(yaml_data)
#print(python_data)
acc = yaml.safe_load(doc)
print("------2------")
print (type(acc))
print(acc)
at = acc['access_token']


# In[ ]:


# TO BE UPDATED
import dicttoxml
import requests  
yang_config = {
    "ietf-interfaces:interface": {
        "name": "Loopback9",
        "description": "Not Out",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4" : {
            "address": [
                {
                    "ip": "10.0.0.99",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}   

print(type(yang_config))

#doc_x = dicttoxml.parseString(yang_config)


# In[ ]:


#### XML Parsing and Regular Expressions -- config example
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML Parsing')
import json
import xmltodict
print('-----1-----')
xml_in = open("netconf_file2.xml").read()
print (type(xml_in))
#### print(xml_in)
print('-----2-----')
doc = xmltodict.parse(xml_in)
#### print(doc)
print (type(doc))
print('-----3-----')
#### pretty output
print(json.dumps(doc, indent=8))
#### FILTERING DATA
#### filter access-token
print('-----4-----')
#### filtered_item = doc["rpc-reply"] => continue filtering in the cell below
filtered_item = doc["rpc-reply"]["data"]["native"]["hostname"]
print(filtered_item)
filtered_item = doc["rpc-reply"]["data"]["native"]["version"]
print(filtered_item)
print('-----5-----')
#### TRANSFORMING DATA TYPES
docs = json.dumps(doc)
print(type(docs))
####
print('-----6-----')
docj = json.loads(docs)
print(type(docj))


# In[ ]:


#### XML Parsing with xml.dom.minidom
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XML Parsing -- xml.dom.minidom')
####
import xml.dom.minidom as xmi
xml_in = xmi.parse("netconf_file2.xml")
print(type(xml_in))
print(xml_in)
#print(xmi.parseString(xml_in).toprettyxml())
print(type(xml_in))
xml_out = xml_in.toprettyxml()
print(type(xml_out))
print(xml_out)
