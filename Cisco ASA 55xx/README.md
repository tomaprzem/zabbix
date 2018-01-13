# Template Cisco ASA 55xx
Templete monitores cpu, memory, traffic etc.  
Template works for me with Cisco ASA 5510 9.1.7

## Requirements

- Zabbix >=3.4
- Configure SNMP in Cisco ASA

## Instalation

- import template to Zabbix
- assign to host
- add macro to host {$SNMP_COMMUNITY}
 
## License

Template Cisco ASA 55xx is licensed under the [MIT License](http://opensource.org/licenses/MIT).  
Copyright 2018 [Przemysław Tomaszewski]
