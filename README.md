# Python NETCONF script for Cisco-XE 

  This python NETCONF script will fetch the ospf configuration from cisco-xe and store the output in XML and JSON format.
   
## 1. Install all required dependencies
  
  Python3 and its dependencies

    pip3 install -r requirements.txt

   
## 2. Update Device Details

Update following Cisco-XE device details for NETCONF.

  - host             => host='ip/domain'
  - port             => port=830
  - username         => username='username'
  - password         => password='password'

## 3. Run the python script

Run the python NETCONF script

    python3 netconf-xe-ospf.py
    
## 4. Check the Result

Check the following files to see the result on output directory

    ospf.xml                       => XML Format
    ospf.json                      => JSON Format
    ospf-interface.xml             => XML Format
    ospf-interface.json            => JSON Format
