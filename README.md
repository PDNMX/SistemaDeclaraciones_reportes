# Sistema de Declaraciones - Reportes

## ⚠️ Precauciones

Nunca exponga los puertos de los componentes internos del Sistema de declaraciones a Internet. Los módulos internos del Sistema de Declaraciones como elasticsearch y el módulo de reportes, pueden ser propensos a sufrir ataques informáticos si se exponen abiertamente en Internet.

Si es posible, utilice el Sistema de Declaraciones a través de una red de área local. Se decide exponer el Sistema de Declaraciones a Internet, revise que únicamente se exponen la dirección del Frontend y el Backend a través de HTTPS.

Evite exponer puertos 9200 (elasticsearch) y 3001 (reporteador) que son usados internamente por el backend del Sistema de Declaraciones.
