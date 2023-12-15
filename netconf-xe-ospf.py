from ncclient import manager
import xml.dom.minidom
import xmltodict
import json

# Creating the NETCONF connection
m = manager.connect(
    host='sandbox-iosxe-latest-1.cisco.com',    # Update XE device ip/domain
    port=830,                                   # Update XE device NETCONF port
    username='admin',                           # Update XE device username
    password='C1sco12345',                      # Update XE device password
    hostkey_verify=False
    )
print(" => NETCONF connection established!")

# Filters for OSPF and OSPF interface config
FILTER_OSPF = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
            <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf"></router-ospf>
        </router>
    </native>
</filter>"""

FILTER_OSPF_INTERFACE = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <ip>
                    <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf"></router-ospf>
                </ip>
            </GigabitEthernet>
        </interface>
    </native>
</filter>"""

# Get and store get_config output of OSPF
running_config_ospf_xml = m.get_config('running', FILTER_OSPF)
running_config_ospf_int_xml = m.get_config('running', FILTER_OSPF_INTERFACE)

# Convert and write to XML file
with open("output/ospf.xml", "w") as ospf_xml_file:
    ospf_xml_file.write(xml.dom.minidom.parseString(str(running_config_ospf_xml)).toprettyxml())

with open("output/ospf-interface.xml", "w") as ospf_int_xml_file:
    ospf_int_xml_file.write(xml.dom.minidom.parseString(str(running_config_ospf_int_xml)).toprettyxml())

# Convert and write to JSON file
running_config_ospf_json = xmltodict.parse(str(running_config_ospf_xml))
running_config_ospf_int_json = xmltodict.parse(str(running_config_ospf_int_xml))

with open("output/ospf.json", "w") as ospf_json_file:
    ospf_json_file.write(json.dumps(running_config_ospf_json, indent=4))

with open("output/ospf-interface.json", "w") as ospf_int_json_file:
    ospf_int_json_file.write(json.dumps(running_config_ospf_int_json, indent=4))

print(" => All files are created successfully!")

# Close the NETCONF connection
m.close_session()
print(" => NETCONF connection closed!")
