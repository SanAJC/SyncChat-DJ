# SyncChat-DJ

SyncChat-DJ es una aplicación de chat en tiempo real construida con Django, Django Channels y WebSockets. Este proyecto permite a los usuarios autenticados unirse a salas de chat, enviar mensajes y recibir actualizaciones instantáneas sin necesidad de recargar la página.

## Características

- **Autenticación con JWT:** Los usuarios deben estar autenticados con un token JWT válido para acceder a las salas de chat.
- **Salas de chat dinámicas:** Los usuarios pueden ver una lista de salas de chat disponibles y unirse a la sala de su elección.
- **Mensajería en tiempo real:** Los mensajes se transmiten en tiempo real utilizando WebSockets, lo que garantiza una experiencia de chat sin interrupciones.
- **Persistencia de mensajes:** Todos los mensajes enviados en las salas se guardan en la base de datos.

## Tecnologías utilizadas

- **Python 3.x**
- **Django 4.x**
- **Django Channels**
- **WebSockets**
- **JavaScript (ES6)**
- **HTML5/CSS3**
- **MariaDB o MySQL**

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/SyncChat-DJ.git
   cd SyncChat-DJ
2. **Crear un entorno virtual e instalar las dependencias:**
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   
3. **Configurar la base de datos**
  El programa corre sobre el servidor de bases de datos Mysql , se debe crear una db con el nombre que esta en settings.py para no tener incoveninetes

4. **Migrar la base de datos:**
  python manage.py migrate

5. **Correr el servidor:**
  python manage.py runserver

   
   
  
   
