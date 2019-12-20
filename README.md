# pruebaDesarrollador

## Lista de objetos
http://localhost:8000/aws/objectsList

## Descargar Objeto
http://localhost:8000/aws/downloadObject?fileName= {{Nombre del archivo con su extension}}
http://localhost:8000/aws/downloadObject?fileName=testfile.txt

## Subir objeto
http://localhost:8000/aws/uploadObject
Nota: la direccion del archivo debe contener forward slashes

{
"fileDir": "C:/test/SalesJan2009.csv",
"saveAs": "SalesJan2009.csv"
}


## Borrar objeto
http://localhost:8000/aws/deleteObject
{
"fileName": "tessdsdt3.txt"
}

## Leer archivo csv desde S3

http://localhost:8000/aws/readCsvObject?fileName={{Nombre del archivo con su extension}}

http://localhost:8000/aws/readCsvObject?fileName=acramentorealestatetransactions.csv
