# ProyectoFinalCoder

Por Juan Cruz Flynn 

## Breve descripción explicativa del proyecto

Este proyecto es llevado a cabo por los alumnos de CoderHouse en el curso de Python.
El proyecto se basa en crear un blog con los conocimientos adquiridos en el transcurso del curso siendo ayudado tanto por el profesor como por los tutores y/o sus compañeros.

## Instalación y ejecución

Puedes descargar el .zip o clonar el repositorio de la siguiente manera:

```bash
git clone https://github.com/Flynn271099/ProyectoFinalCoder.git
```
Luego deberá instalar y crear un entorno virtual en donde podrá manipular el proyecto:
```bash
cd ProyectoFinalCoder
pip install virtualenv
python -m virtualenv "venv"  
"venv"\Scripts\activate
```
También al iniciar el entorno virtual deberemos realizar los siguentes pasos:
```bash
pip install django
pip install pillow
```
Para que todo funcione con normalidad.

El "venv" referenciado en el código anterior puede ser modificado de nombre a gusto y no debe incluir las comillas.

## Funciones

Para poder interactuar con el proyecto deberemos iniciarlo de la siguiente manera:

```python
cd Blog
python manage.py runserver
```
En caso de que hayan seguido correctamente los pasos se iniciará el Blog en un servidor web el cual tendrán acceso por un link numerico en su terminal. 

¡Ahora sí! Puedes gestionar a gusto el sitio y el mismo cuenta con un panel admin de Django el cual podrá manipular con el usuario "flynn" y contraseña "Facundo12345".

El sitio cuenta con 3 ingresos de datos: Añadir Empleado, Jefe y Cliente, gestionar la actualización, eliminación y ver los detalles de los Empleados y Jefes, por último contiene una página donde te permitirá buscar a los clientes ingresados por su email. 

A su vez tendrán un botón en la barra de navegación "Sobre Mí" el cual contiene un poco de información sobre mi persona y lo que hago actualmente.

Por último encontrarán las opciones para Registrarse, Iniciar Sesión, Cerrar sesión y en caso de ser usuario administrativo/Staff podrán ver el botón de "Admin" el cual los enviará a la gestión administrativa de Django por parte del Blog.

# Créditos

¡Muchas gracias a CoderHouse y más que nada al [Profesor] Daniel Ochoa y a la [Tutora] Maria Emilia Díaz! Tanto el profesor en clase como la tutora en after o dudas por mensajes privados en la web de Coder me han servido para mantener el ritmo, aprender con mas sultura el lenguaje y poder comprender un poco más del código en general al momento de crearlo, leerlo y modificarlo.

Es muy posible que no cumpla con los requisitos de la entrega debido a tiempo que no he tenido por cuestiones personales y laborales pero espero que les guste. 
