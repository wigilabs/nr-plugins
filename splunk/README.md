# Splunk


> Utilize el SDK de splunk para extraer los datos de monitoreo y logs.

Clone este repositorio y añada las siguientes lineas a las tares de cron ( Utilice el comando crontab -e).
```sh
* * * * * python /opt/splunk-sdk-python/examples/apacheErrors.py 'search source="/var/log/apache2/error.log" host="debian-splunk" sourcetype="apache_error" | HEAD 1' --output_mode=json
* * * * * python /opt/splunk-sdk-python/examples/apacheAccess.py 'search source="/var/log/apache2/access.log" host="debian-splunk" index="history" sourcetype="access" | HEAD 1' --output_mode=json
* * * * * python /opt/splunk-sdk-python/examples/kernelStatus.py 'search source="/var/log/kern.log" host="debian-splunk" index="history" sourcetype="kernel_status" | HEAD 1' --output_mode=json
* * * * * python /opt/splunk-sdk-python/examples/systemctlLog.py 'search source="/var/log/syslog" host="debian-splunk" sourcetype="systemctl" | HEAD 1' --output_mode=json
```
**WARNING: No garantizo que estos scripts funcionen al 100%! Todos ellos se encuentran en distintas etapas de desarrollo asegurese de seguir las intrucciones tal como se indica o utilice los scripts de instalacion bajo su propio riesgo!**

**WARNING: Estas consultas siguen un estandar predeterminado para el monitoreo de logs, depende de la data que se quiera monitorear la configuracion puede variar.**
