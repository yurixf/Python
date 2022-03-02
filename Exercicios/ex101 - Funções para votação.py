def votar(nasc):
    from datetime import date
    idade = date.today().year-nasc
    if idade<16:
        return f'Com {idade} anos, Não Vota'
    elif idade <18 or idade>65:
        return f'Com {idade} anos, o Voto Opcional'
    else:
        return f'Com {idade} anos, o voto é Obrigatório'


ano = int(input('Ano de Nascimento:'))
print(votar(ano))