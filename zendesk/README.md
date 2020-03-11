# Zendesk

> Utilize la libreria zenpy para obtener data de su cuenta de zendesk y enviarla a newrelic.

Instale los requerimientos.
```sh
pip install -r requeriments.txt
```
ubique los dos archivos ejecutables en /bin y ejecute la siguiente linea de comando.
```sh
export PATH=$PATH:/bin/zendesk.sh
```
En la carpeta sample encontrara un template para ejecutar su script de forma automatica, cree el daemon  en la siguiente ruta
/etc/systemd/system.

Una vez complete estos pasos, ejecute los siguientes comandos para automatizar los procesos.
```sh
systemctl enable zendesk.service
systemctl start zendesk.service
```


**WARNING: No garantizo que estos scripts funcionen al 100%! Todos ellos se encuentran en distintas etapas de desarrollo asegurese de seguir las intrucciones tal como se indica o utilice los scripts de instalacion bajo su propio riesgo!**

**WARNING: Estas consultas siguen un estandar predeterminado para el monitoreo de logs, depende de la data que se quiera monitorear la configuracion puede variar.**
