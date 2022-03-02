def fatorial(n, show=False):
    """

    :param n: o valor que vai ser calculada a Fatorial
    :param show: (opcional) Mostrar todos os valores do calculo
    :return: o valor do fatorial de n
    """
    from math import factorial
    print('-' * 30)
    f = factorial(n)
    if show == True:
        print(n, '* ', end='')
        while n != 1:
            n -= 1
            if n > 1:
                print(n, end=' * ')
            else:
                print(n, end=' = ')
    return f


print(fatorial(5))
help(fatorial)
