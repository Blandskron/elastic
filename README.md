# Documentación del Proyecto

Este proyecto incluye una colección de solicitudes para interactuar con Elasticsearch y un archivo de configuración de Docker Compose para ejecutar Elasticsearch en un contenedor. A continuación se presenta una descripción detallada de cada archivo.

## 1. Colección de Postman para Elasticsearch

La colección de Postman se utiliza para realizar varias operaciones en un índice de Elasticsearch. A continuación se describen las solicitudes disponibles:

### Solicitudes en la Colección

1. **Crear índice**
   - **Método**: `PUT`
   - **URL**: `http://localhost:9200/my_index`
   - **Cuerpo**:
     ```json
     {
       "settings": {
         "number_of_shards": 1,
         "number_of_replicas": 1
       }
     }
     ```

2. **Verificar índice**
   - **Método**: `GET`
   - **URL**: `http://localhost:9200/my_index`

3. **Agregar documento 1**
   - **Método**: `POST`
   - **URL**: `http://localhost:9200/my_index/_doc/1`
   - **Cuerpo**:
     ```json
     {
       "name": "John Doe",
       "age": 30,
       "email": "johndoe@example.com"
     }
     ```

4. **Agregar documento 2**
   - **Método**: `POST`
   - **URL**: `http://localhost:9200/my_index/_doc/2`
   - **Cuerpo**:
     ```json
     {
       "name": "Jane Smith",
       "age": 25,
       "email": "janesmith@example.com"
     }
     ```

5. **Buscar todos los documentos**
   - **Método**: `GET`
   - **URL**: `http://localhost:9200/my_index/_search`

6. **Buscar por nombre**
   - **Método**: `GET`
   - **URL**: `http://localhost:9200/my_index/_search`

7. **Actualizar documento**
   - **Método**: `POST`
   - **URL**: `http://localhost:9200/my_index/_update/1`
   - **Cuerpo**:
     ```json
     {
       "doc": {
         "age": 31
       }
     }
     ```

8. **Eliminar documento**
   - **Método**: `DELETE`
   - **URL**: `http://localhost:9200/my_index/_doc/1`

9. **Eliminar índice**
   - **Método**: `DELETE`
   - **URL**: `http://localhost:9200/my_index`

### Requisitos

- Tener Postman instalado para importar y realizar las solicitudes.

## 2. Docker Compose para Elasticsearch

El archivo `docker-compose.yml` se utiliza para configurar y ejecutar una instancia de Elasticsearch en un contenedor Docker. A continuación se describen las configuraciones principales:

### Configuración del Contenedor

- **Imagen**: `docker.elastic.co/elasticsearch/elasticsearch:8.10.2` (Última versión de Elasticsearch)
- **Nombre del contenedor**: `es01`
- **Configuraciones del entorno**:
  - `node.name`: Nombre del nodo en el cluster.
  - `cluster.name`: Nombre del cluster.
  - `cluster.initial_master_nodes`: Nodos maestros iniciales.
  - `bootstrap.memory_lock`: Asegura que la memoria no sea intercambiada.
  - `ES_JAVA_OPTS`: Opciones de Java para la configuración de memoria.
  - `xpack.security.enabled`: Desactivado para pruebas (no recomendado en producción).

### Volúmenes y Redes

- **Volumen**: `data01` se utiliza para persistir los datos de Elasticsearch.
- **Red**: Se utiliza la red `elastic` con el controlador `bridge`.

### Cómo Ejecutar

1. Asegúrate de tener Docker y Docker Compose instalados.
2. En la terminal, navega hasta el directorio donde se encuentra el archivo `docker-compose.yml`.
3. Ejecuta el siguiente comando para iniciar Elasticsearch:
   ```bash
   docker-compose up
   ```
4. Accede a Elasticsearch en `http://localhost:9200`.

## Conclusión

Este proyecto proporciona una forma fácil de interactuar con Elasticsearch utilizando Postman y Docker. Asegúrate de seguir las instrucciones y ajustar las configuraciones según sea necesario para tus requerimientos.
