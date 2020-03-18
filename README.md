# Nr-plugins

> Utilize la libreria zenpy para obtener data de su cuenta de zendesk y enviarla a newrelic.

Instale los requerimientos.
```sh
pip install -r requeriments.txt
```
Para terminar la configuracion añada sus scripts a un gestor de tareas en linux como crontabs, utilize el siguiente comando:
```sh
crontabs -e
```
Se abrira un editor de texto donde debera agregar su script y la frecuencia con la cual se va ha utilizar, por ejemplo:
```sh
* * * * * python script.py
```
> script.py se ejecutara cada 60 segundos.
**WARNING: No garantizo que estos scripts funcionen al 100%! Todos ellos se encuentran en distintas etapas de desarrollo asegurese de seguir las intrucciones tal como se indica o utilice los scripts de instalacion bajo su propio riesgo!**

**WARNING: Estas consultas siguen un estandar predeterminado para el monitoreo de logs, depende de la data que se quiera monitorear la configuracion puede variar.**
