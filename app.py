from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Crear aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'  # Necesario para los formularios con CSRF

# Definir el formulario
class MiFormulario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta del formulario
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = MiFormulario()
    if form.validate_on_submit():
        nombre = form.nombre.data
        return render_template('resultado.html', nombre=nombre)
    return render_template('formulario.html', form=form)

# Ruta de "Acerca de"
@app.route('/about')
def about():
    return render_template('about.html')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
