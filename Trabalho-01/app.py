from flask import Flask, render_template, request, redirect, url_for
from filtros import aplicar_filtro
import os

app = Flask(__name__)

# Configurações de diretórios
UPLOAD_FOLDER = os.path.join('static', 'uploads')
PROCESSED_FOLDER = os.path.join('static', 'processed')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verifica se veio arquivo
        file = request.files.get('imagem')
        filtro = request.form.get('filtro')
        if not file or filtro is None:
            return redirect(request.url)

        # Salva upload
        filename = file.filename
        caminho_upload = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(caminho_upload)

        # Aplica filtro
        caminho_saida = os.path.join(app.config['PROCESSED_FOLDER'], filename)
        aplicar_filtro(caminho_upload, caminho_saida, filtro)

        return render_template('index.html', original=url_for('static', filename=f'uploads/{filename}'),
                                              processada=url_for('static', filename=f'processed/{filename}'))
    return render_template('index.html')

if __name__ == '__main__':
    # Cria pastas se não existirem
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    app.run(debug=True)