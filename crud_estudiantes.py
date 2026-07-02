import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ── BASE DE DATOS ──────────────────────────────
conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre  TEXT    NOT NULL,
        carrera TEXT    NOT NULL,
        nota    REAL    NOT NULL
    )
""")
conexion.commit()

# ── FUNCIONES CRUD ─────────────────────────────

def leer():
    """Carga todos los registros en la tabla visual"""
    for fila in tabla.get_children():
        tabla.delete(fila)
    cursor.execute("SELECT * FROM estudiantes")
    for registro in cursor.fetchall():
        tabla.insert("", tk.END, values=registro)

def agregar():
    """Lee los campos y guarda un nuevo estudiante"""
    nombre  = entry_nombre.get().strip()
    carrera = entry_carrera.get().strip()
    nota    = entry_nota.get().strip()

    if not nombre or not carrera or not nota:
        messagebox.showwarning("Aviso", "Completa todos los campos.")
        return

    try:
        cursor.execute(
            "INSERT INTO estudiantes (nombre, carrera, nota) VALUES (?, ?, ?)",
            (nombre, carrera, float(nota))
        )
        conexion.commit()
        leer()
        limpiar_campos()
    except ValueError:
        messagebox.showerror("Error", "La nota debe ser un numero.")

def editar():
    """Actualiza el registro seleccionado en la tabla"""
    seleccion = tabla.focus()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un estudiante de la tabla.")
        return
    id_sel = tabla.item(seleccion)["values"][0]
    try:
        cursor.execute(
            "UPDATE estudiantes SET nombre=?, carrera=?, nota=? WHERE id=?",
            (entry_nombre.get(), entry_carrera.get(), float(entry_nota.get()), id_sel)
        )
        conexion.commit()
        leer()
        limpiar_campos()
    except ValueError:
        messagebox.showerror("Error", "La nota debe ser un numero.")

def eliminar():
    """Elimina el registro seleccionado con confirmacion"""
    seleccion = tabla.focus()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un estudiante de la tabla.")
        return
    id_sel = tabla.item(seleccion)["values"][0]
    conf = messagebox.askyesno("Confirmar", "Eliminar este estudiante?")
    if conf:
        cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_sel,))
        conexion.commit()
        leer()
        limpiar_campos()

def seleccionar_fila(event):
    """Al hacer clic en la tabla, carga los datos en los campos"""
    seleccion = tabla.focus()
    if seleccion:
        valores = tabla.item(seleccion)["values"]
        limpiar_campos()
        entry_nombre.insert(0, valores[1])
        entry_carrera.insert(0, valores[2])
        entry_nota.insert(0, valores[3])

def limpiar_campos():
    """Vacia los campos de texto"""
    entry_nombre.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# ── VENTANA ────────────────────────────────────
ventana = tk.Tk()
ventana.title("Sistema de Estudiantes — ITB")
ventana.geometry("680x500")
ventana.resizable(True, True)

# ── CAMPOS DE ENTRADA ──────────────────────────
tk.Label(ventana, text="Nombre:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_nombre = tk.Entry(ventana, width=35, font=("Arial", 11))
entry_nombre.grid(row=0, column=1, padx=10, pady=8, columnspan=2)

tk.Label(ventana, text="Carrera:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_carrera = tk.Entry(ventana, width=35, font=("Arial", 11))
entry_carrera.grid(row=1, column=1, padx=10, pady=8, columnspan=2)

tk.Label(ventana, text="Nota:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="e")
entry_nota = tk.Entry(ventana, width=15, font=("Arial", 11))
entry_nota.grid(row=2, column=1, padx=10, pady=8, sticky="w")

# ── BOTONES ────────────────────────────────────
frame_btns = tk.Frame(ventana)
frame_btns.grid(row=3, column=0, columnspan=3, pady=10)

tk.Button(frame_btns, text="Agregar",    bg="#2d6a4f", fg="white", command=agregar,  width=12).grid(row=0, column=0, padx=5)
tk.Button(frame_btns, text="Editar",     bg="#1d3557", fg="white", command=editar,   width=12).grid(row=0, column=1, padx=5)
tk.Button(frame_btns, text="Eliminar",   bg="#9e2a2b", fg="white", command=eliminar, width=12).grid(row=0, column=2, padx=5)
tk.Button(frame_btns, text="Actualizar", bg="#555",    fg="white", command=leer,     width=12).grid(row=0, column=3, padx=5)

# ── TABLA (TREEVIEW) ───────────────────────────
cols = ("ID", "Nombre", "Carrera", "Nota")
tabla = ttk.Treeview(ventana, columns=cols, show="headings", height=12)

for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=140 if col != "ID" else 50)

tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
tabla.bind("<<TreeviewSelect>>", seleccionar_fila)

scroll = ttk.Scrollbar(ventana, orient="vertical", command=tabla.yview)
scroll.grid(row=4, column=3, sticky="ns", pady=10)
tabla.configure(yscrollcommand=scroll.set)

ventana.grid_rowconfigure(4, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# ── INICIO ─────────────────────────────────────
leer()
ventana.mainloop()
