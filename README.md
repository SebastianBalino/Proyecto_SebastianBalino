# Proyecto_SebastianBalino
README - Django 
Este proyecto es una aplicación web desarrollada con Django para gestionar productos, clientes, contactos y usuarios. A continuación, se ofrece una descripción detallada de las vistas y formularios del proyecto, que cubren funcionalidades como el manejo de productos, el registro de usuarios y clientes, así como la autenticación de usuarios.

Funcionalidades
1. Vistas Generales
inicio(request)
Vista de inicio que renderiza la página principal del sitio web.
Plantilla: index.html

sobremi(request)
Vista que renderiza la página "Sobre mí", destinada a proporcionar información sobre el negocio o el propietario.
Plantilla: sobremi.html

clientes(request)
Vista que muestra la información relacionada con los clientes.
Plantilla: clientes.html

productos(request)
Vista para mostrar la página principal de productos.
Plantilla: productos.html

contacto(request)
Vista para mostrar la página de contacto, donde los usuarios pueden enviar mensajes.
Plantilla: contacto.html

2. Gestión de Productos
agregar_producto(request)
Permite agregar nuevos productos a la base de datos. Si el formulario es válido, el producto se guarda en la base de datos y se redirige a la página de agregar productos nuevamente.
Plantilla: agregar_producto.html

actualizar_producto(request, producto_id)
Permite actualizar la información de un producto específico mediante su producto_id. Si la solicitud es POST y el formulario es válido, se guarda el producto actualizado.
Plantilla: producto_form.html

eliminar_producto(request, producto_id)
Permite eliminar un producto específico de la base de datos. La eliminación se realiza tras una confirmación con un formulario POST.
Plantilla: eliminar_producto.html

productos_lista(request)
Muestra todos los productos disponibles en la base de datos.
Plantilla: productos_lista.html

buscar_producto(request)
Permite realizar búsquedas de productos en función del nombre y la descripción. El formulario filtra los productos según los valores introducidos.
Plantilla: buscar_producto.html

3. Gestión de Clientes
registrar_cliente(request)
Permite registrar nuevos clientes en la base de datos. Si el formulario es válido, se guarda la información del cliente y se redirige a la lista de clientes.
Plantilla: registrar_cliente.html
4. Gestión de Contactos
contacto(request)
Permite a los usuarios enviar mensajes de contacto. Si el formulario es válido, se guarda la información del mensaje y se redirige al usuario a una página de confirmación.
Plantilla: contacto.html
5. Autenticación de Usuarios
login_request(request)
Permite a los usuarios iniciar sesión en el sistema. Si las credenciales son correctas, el usuario es autenticado y se le redirige a la página de inicio. Si las credenciales son incorrectas, se muestra un mensaje de error.
Plantilla: login.html

register(request)
Permite registrar nuevos usuarios en el sistema. Si el formulario es válido, se crea un nuevo usuario y se redirige al usuario a la página de inicio.
Plantilla: registro.html

Formularios
1. Formulario de Producto
ProductoForm(forms.ModelForm)
Este formulario se utiliza para crear o editar productos. Permite ingresar el nombre, descripción, precio y cantidad de un producto.
Campos: nombre, descripcion, precio, cantidad
2. Formulario de Contacto
ContactoForm(forms.ModelForm)
Formulario que permite a los usuarios enviar mensajes de contacto.
Campos: nombre, email
3. Formulario de Cliente
ClienteForm(forms.ModelForm)
Formulario que permite registrar nuevos clientes.
Campos: nombre, email, telefono, direccion
4. Formulario de Búsqueda de Producto
ProductoSearchForm(forms.Form)
Permite a los usuarios buscar productos por nombre o descripción.
Campos: nombre, descripcion
5. Formulario de Registro de Usuario
UserRegisterForm(forms.ModelForm)
Formulario que permite a los usuarios registrarse en el sistema con un nombre de usuario, correo electrónico y contraseña.
Campos: username, email, password1, password2

Archivos de Plantillas
El proyecto utiliza las siguientes plantillas HTML para representar las vistas en la interfaz de usuario:

index.html: Página de inicio del sitio.
sobremi.html: Página que describe la información sobre el negocio o propietario.
clientes.html: Página que muestra la información de los clientes.
productos.html: Página que presenta los productos.
contacto.html: Página de contacto para enviar consultas.
agregar_producto.html: Página que permite agregar productos al sistema.
producto_form.html: Página que permite actualizar un producto existente.
eliminar_producto.html: Página para confirmar la eliminación de un producto.
productos_lista.html: Página que muestra la lista de todos los productos disponibles.
buscar_producto.html: Página de búsqueda de productos.
registrar_cliente.html: Página para registrar nuevos clientes.
login.html: Página de inicio de sesión para usuarios.
registro.html: Página de registro para nuevos usuarios.