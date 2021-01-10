filmes = {
    'drama': ['Cidadão Kane', 'O poderoso Chefão'],
    'comedia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}
with open('filmes.html', 'w', encoding='utf-8') as pagina:
    pagina.write('''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Filmes</title>
    </head>
    <body>
    
    </body>
    </html>
    ''')
    for c, v in filmes.items():
        pagina.write(f'<h1>{c}</h1>\n')
        pagina.write('<ul>\n')
        for e in v:
            pagina.write(f'<li>{e}</li>\n')
        pagina.write('</ul>\n')
    pagina.write('</body></html>')
