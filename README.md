# zbx_maxscale
Zabbix-Checks for MaxScale

Installation:
Copy maxscale_discovery.py and maxscale_status.py to the zabbix-server external-scripts directory.
Install click and requests using pip:
pip install click
pip install requests

Import the 
template-maxscale.xml

Assign the template to the host where maxscale is installed.
