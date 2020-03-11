## Zabbix API

Este script le permitira extraer data humanamente legible por medio del API REST de zabbix, para configurar este script con su cuenta debera disponer de su nombre de usuario, contraseña nombre de host donde esta ejecutando zabbix, este script extrae la data y la envia a newrelic por lo que tambien debera disponer de una cuenta en newrelic para su correcto funcionamiento.
```sh
9  | API='http://<HOST>/zabbix/api_jsonrpc.php'
10 | data = {'jsonrpc': '2.0', 'method': 'user.login', 'params': {  "user": "<USERNAME>", "password": "<PASSWORD>"},"id": 1 }
```
