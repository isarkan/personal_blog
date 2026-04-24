# Personal Blog - CRUD con Arquitectura en Capas (Onion)

Este es un pequeño proyecto de **blog personal** desarrollado con el objetivo de **aprender y practicar la arquitectura de cebolla (Onion Architecture)**.  

La aplicación implementa un **CRUD completo de artículos** (crear, listar, editar y eliminar) y está organizada en capas para separar responsabilidades:

- **Dominio:** Entidad `Articulo` y repositorio abstracto.  
- **Aplicación:** Casos de uso para gestionar artículos.  
- **Infraestructura:** Implementación en memoria del repositorio.  
- **Presentación:** Interfaz web con Flask, plantillas HTML y estilos CSS.  

### Objetivo
El propósito principal de este proyecto es **entender cómo estructurar aplicaciones modulares y escalables**, aplicando buenas prácticas de separación de capas y patrones de repositorio.

### Funcionalidades
- Crear artículos desde un formulario.  
- Listar artículos en la página principal.  
- Ver detalle de cada artículo.  
- Editar y eliminar artículos desde el panel de administración.  
- Interfaz web estilizada con HTML y CSS.  
