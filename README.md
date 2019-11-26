# zbx_maxscale
Zabbix-Checks for MaxScale

Prerequisites:
maxscale must be running and the rest api must be reachable from zabbix-server. This can be achieved setting the admin_host configuration in the maxscale section.

Installation:

Copy maxscale_discovery.py and maxscale_status.py to the zabbix-server external-scripts directory.
Install click and requests using pip:

pip install click

pip install requests

Import the 
template-maxscale.xml

Assign the template to the host where maxscale is installed.

### Credits
Inspired and based on the work of Arthur Dali
https://share.zabbix.com/cat-app/high-availability-ha/maxscale-script-discovery
