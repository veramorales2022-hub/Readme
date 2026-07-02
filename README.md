# 🎓 Sistema de Gestión de Estudiantes

Aplicación de escritorio desarrollada en **Python** utilizando **Tkinter** para la interfaz gráfica y **SQLite3** como base de datos. Permite gestionar estudiantes mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

---

## 📋 Características

* ➕ Agregar nuevos estudiantes.
* ✏️ Editar información existente.
* 🗑️ Eliminar estudiantes con confirmación.
* 🔄 Actualizar la lista de registros.
* 📊 Visualización de los datos mediante una tabla (`Treeview`).
* 💾 Base de datos SQLite creada automáticamente.
* ✔️ Validación de los datos ingresados.

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Tkinter
* SQLite3

---

## 📁 Estructura del proyecto

```text
Sistema-Estudiantes/
│
├── main.py
├── estudiantes.db
├── README.md
└── .gitignore (opcional)
```

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/Sistema-Estudiantes.git
```

### 2. Entrar en la carpeta del proyecto

```bash
cd Sistema-Estudiantes
```

### 3. Ejecutar la aplicación

```bash
python main.py
```

---

## 🖥️ Uso de la aplicación

1. Ingresa el **nombre** del estudiante.
2. Escribe la **carrera**.
3. Ingresa la **nota**.
4. Haz clic en **Agregar** para guardar el registro.
5. Selecciona un estudiante de la tabla para **Editar** o **Eliminar** su información.
6. Presiona **Actualizar** para recargar los datos de la base de datos.

---

## 🗄️ Base de datos

La aplicación crea automáticamente el archivo:

```text
estudiantes.db
```

Con la siguiente estructura:

| Campo   | Tipo                              |
| ------- | --------------------------------- |
| id      | INTEGER PRIMARY KEY AUTOINCREMENT |
| nombre  | TEXT                              |
| carrera | TEXT                              |
| nota    | REAL                              |

---

## 📷 Captura de pantalla

Puedes agregar una imagen de la aplicación para mostrar su funcionamiento.

Ejemplo:

```text
Sistema-Estudiantes/
│
├── screenshots/
│   └── interfaz.png
```

Luego agrega la siguiente línea en este README:

```md
![Interfaz del Sistema](screenshots/interfaz.png)
```

---

## 🔮 Mejoras futuras

* 🔍 Buscar estudiantes por nombre.
* 📊 Ordenar registros por nota o carrera.
* 📄 Exportar datos a Excel.
* 📑 Exportar datos a PDF.
* 🌙 Implementar modo oscuro.
* 📈 Mostrar estadísticas y promedio de notas.
* 🖨️ Imprimir reportes.

---

## 👨‍💻 Autor

**Alexander Vera Morales**

Proyecto desarrollado como práctica académica para aprender el uso de Python, Tkinter y SQLite en la creación de aplicaciones de escritorio con operaciones CRUD.

---

## 📄 Licencia

Este proyecto es de uso educativo y puede modificarse libremente con fines de aprendizaje.
