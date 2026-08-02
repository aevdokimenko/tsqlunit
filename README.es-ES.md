

# Resumen

TSQLUnit es un marco de trabajo para escribir pruebas para aplicaciones escritas en Transact-SQL. Sigue la tradición del marco "xUnit", que está disponible para casi todos los lenguajes de programación.

## Instalación
1. Descomprima el archivo. Puede usar WinZip o el software de código abierto 7-zip. 
2. Conéctese a su base de datos como dbo usando el SQL Query Analyzer y ejecute el archivo tsqlunit.sql. 

## Desinstalación
1. Conéctese a su base de datos como dbo usando el SQL Query Analyzer y ejecute el archivo removetsqlunit.sql.

## Proyecto original
**Autor**: [Henrik Ekelund](https://sourceforge.net/u/ekelund/profile/)  
**Espacio del proyecto en Sourceforge**: [TSQLUnit](https://sourceforge.net/projects/tsqlunit/)

## Historial de versiones
### Versión 0.92
1. Agrega la función Assert

### Versión 0.91 de corrección de errores
Errores corregidos:
1. Limitación del mensaje de fallo		
2. La línea 43 del proc tsu_error genera errores	
3. No se puede instalar en DB con collation %_CS_%  (sensible a mayúsculas y minúsculas)	
4. El nombre del conjunto de pruebas no se muestra en la salida	
5. Nombres de columnas y SP mal escritos	
6. Problema con la reversión (rollback) de la transacción	
7. Devolver éxito o fallo al completar x	

### Versión original 0.9
--
