## Zabbix API
> Utilize el api oficial de zabbix para enviar data a newrelic.

Este script le permitira extraer data humanamente legible por medio del API REST de zabbix, para configurar este script con su cuenta debera disponer de su nombre de usuario, contraseña nombre de host donde esta ejecutando zabbix, este script extrae la data y la envia a newrelic por lo que tambien debera disponer de una cuenta en newrelic para su correcto funcionamiento.

```sh
7  | nrheaders={'Content-type': 'application/json', 'x-insert-key' : '<NEWRELIC_API_KEY>'}
8  | nrAPI='https://insights-collector.newrelic.com/v1/accounts/<ACCOUNT_ID>/events'
9  | API='http://<HOST>/zabbix/api_jsonrpc.php'
10 | data = {'jsonrpc': '2.0', 'method': 'user.login', 'params': {  "user": "<USERNAME>", "password": "<PASSWORD>"},"id": 1 }
```
**Advertencia: No garantizo que estos scripts funcionen al 100%! Todos ellos se encuentran en distintas etapas de desarrollo asegurese de seguir las intrucciones tal como se indica o utilice los scripts de instalacion bajo su propio riesgo!**
