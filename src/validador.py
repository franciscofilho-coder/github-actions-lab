def limpar_cpf(cpf: str) -> str:
    '''Remove pontos, traços e espaços de um CPF'''
    return ''.join(c for c in cpf if c.isdigit())

def validar_cpf(cpf: str) -> bool:
    '''Valida o CPF checando os dígitos verificadores'''
    cpf = limpar_cpf(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True
