with open('index.html', 'w', encoding='utf-8') as pagina:
    pagina.write('<DOCTYPE html>\n')
    pagina.write('<html lang="pt-BR">\n')
    pagina.write('<head>\n')
    pagina.write('<meta charset="utf-8">\n')
    pagina.write('<title>Tìtulo da página</title>\n')
    pagina.write('</head>\n')
    pagina.write('<body>\n')
    pagina.write('Olá!')
    for l in range(101):
        pagina.write(f'<p>{l} {l+1} {l+2}</p>')
    pagina.write('</body>\n')
    pagina.write('</html>\n')
