def notas(*n, sit=False):
    """
    :param n: notas dos alunos
    :param sit:(opcional) Mostra a situação do aluno
    :return:retorna um dicionario com a quantidade de notas, a maior, a menor, a media e a situação
    """
    aluno = {}
    total=maior=menor=0
    aluno['total']=len(n)
    aluno['maior']= max(n)
    aluno['menor']=min(n)
    aluno['media']=sum(n)/len(n)
    if sit:
        if aluno['media']>=7:
            aluno['situação']='Boa'
        elif aluno['media']<=5:
            aluno['situação']='Ruim'
        else:
            aluno['situação']='Rázoavel'
    return f'{aluno}'


resp = notas(5,7,4,10,10,7, sit=True)
print(resp)
help(notas)