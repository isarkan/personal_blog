from flask import Flask, render_template, request, redirect
from infraestructura.repositorio.art_repo_memoria import ArticuloRepositorioMemoria
from aplicacion.casos_uso.listar_art import ListarArticulos
from aplicacion.casos_uso.crear_art import CrearArticulo
from aplicacion.casos_uso.editar_art import EditarArticulo
from aplicacion.casos_uso.eliminar_art import EliminarArticulo

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
repo = ArticuloRepositorioMemoria()

@app.route('/')
def inicio():
    casos = ListarArticulos(repo)
    articulos = casos.ejecutar()
    return render_template('index.html', articulos=articulos)

@app.route('/articulo/<int:id>')
def ver_articulo(id):
    articulo = repo.obtener_por_id(id)
    return render_template('articulo.html', articulo=articulo)


@app.route('/admin')
def admin():
    articulos = repo.obtener_todos()
    return render_template('admin.html', articulos=articulos)

@app.route('/admin/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']

        caso = CrearArticulo(repo)
        caso.ejecutar(titulo, contenido)

        return redirect('/admin')

    return render_template('crear.html')

@app.route('/admin/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']

        caso = EditarArticulo(repo)
        caso.ejecutar(id, titulo, contenido)

        return redirect('/admin')

    articulo = repo.obtener_por_id(id)
    return render_template('editar.html', articulo=articulo)

@app.route('/admin/eliminar/<int:id>')
def eliminar(id):
    caso = EliminarArticulo(repo)
    caso.ejecutar(id)
    return redirect('/admin')