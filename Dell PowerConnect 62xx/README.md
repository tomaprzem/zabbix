# Template Dell 62xx
Templete monitors cpu, memory, temperature, fans, power, poe etc.  
To monitors traffic add builtin Zabbix 3.4 template Template Module Interfaces Simple SNMP  
Template works fine for me with Dell 6248 and 6248P v3.3.17

## Requirements

- Zabbix >=3.4
- Dell PowerConnect version >= 3.0.0

## Instalation

- import template to Zabbix
- assign to host
- add macro {$SNMP_COMMUNITY} to host
 
## License

Template Template Dell 62xx is licensed under the [MIT License](http://opensource.org/licenses/MIT).  
Copyright 2018 [Przemysław Tomaszewski]
