from PIL import Image, ImageFilter, ImageOps

# Filtro Negativo
def filtro_negativo(im):
    return ImageOps.invert(im)

# Filtro da Mediana
def filtro_mediana(im, tamanho=3):
    return im.filter(ImageFilter.MedianFilter(size=tamanho))

# Filtro Gaussiano
def filtro_gaussiano(im, raio=2):
    return im.filter(ImageFilter.GaussianBlur(radius=raio))

# Filtro Sépia (personalizado)
def filtro_sepia(im):
    # Converte para escala de cinza
    cinza = im.convert('L')
    # Aplica tonificação sépia
    sepia = ImageOps.colorize(cinza, '#704214', '#C0A080')
    return sepia

# Função principal para aplicar filtros
def aplicar_filtro(caminho_entrada, caminho_saida, filtro_nome):
    im = Image.open(caminho_entrada).convert('RGB')
    if filtro_nome == 'negativo':
        out = filtro_negativo(im)
    elif filtro_nome == 'mediana':
        out = filtro_mediana(im)
    elif filtro_nome == 'gaussiano':
        out = filtro_gaussiano(im)
    elif filtro_nome == 'sepia':
        out = filtro_sepia(im)
    else:
        out = im
    out.save(caminho_saida)