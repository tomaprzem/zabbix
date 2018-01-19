# Template Dell 54xx
Templete monitors cpu, memory, temperature, fans, power etc.  
To monitors traffic add builtin Zabbix 3.4 template Template Module Interfaces Simple SNMP  
Template works fine for me with Dell 5448 v2.0.0.46

## Requirements

- Zabbix >=3.4
- Dell PowerConnect version >= 2.0.0

## Instalation

- import template to Zabbix
- assign to host
- add macro {$SNMP_COMMUNITY} to host
 
## License

Template Template Dell 54xx is licensed under the [MIT License](http://opensource.org/licenses/MIT).  
Copyright 2018 [Przemysław Tomaszewski]
