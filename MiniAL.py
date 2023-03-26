import re

# Define uma expressão regular para cada tipo de token
regex_identificador = r'[a-zA-Z]+'
regex_numero_inteiro = r'[0-9]+'
regex_numero_real = r'[0-9]+\.[0-9]+'
regex_soma = r'\+'
regex_subtracao = r'-'
regex_multiplicacao = r'\*'
regex_divisao = r'/'
# regex_operadores = r'[+\-*/]'
regex_atribuicao = r'='
regex_parenteses = r'[()]'
regex_fim_de_linha = r'\n'

# Associa cada expressão regular a um nome de token
tokens = {
    'IDENTIFICADOR': regex_identificador,
    'NUMERO_INTEIRO': regex_numero_inteiro,
    'NUMERO_REAL': regex_numero_real,
    'OPERADOR_SOMA': regex_soma,
    'OPERADOR_SUBTRACAO': regex_subtracao,
    'OPERADOR_MULTIPLICACAO': regex_multiplicacao,
    'OPERADOR_DIVISAO': regex_divisao,
    'ATRIBUICAO': regex_atribuicao,
    'ABRE_PARENTESES': regex_parenteses,
    'FECHA_PARENTESES': regex_parenteses,
    'FIM_DE_LINHA': regex_fim_de_linha,
}

# Função para analisar uma expressão
def analisar(expressao):
    # Adiciona um espaço no final da expressão para facilitar a análise
    expressao = expressao.strip() + ' '

    # Inicializa as variáveis de estado
    posicao = 0
    tokens_encontrados = []
    erros = []

    # Enquanto não chegamos no final da expressão
    while posicao < len(expressao):
        # Ignora espaços em branco e quebras de linha
        if expressao[posicao] in [' ', '\n']:
            posicao += 1
            continue

        # Tenta casar a entrada com cada expressão regular
        match = None
        for nome, regex in tokens.items():
            match = re.match(regex, expressao[posicao:])
            if match:
                valor = match.group(0)
                if nome == 'IDENTIFICADOR':
                    # Se for um identificador, adiciona à lista de tokens encontrados
                    # e registra seu índice na tabela de símbolos
                    if valor not in tabela_simbolos:
                        tabela_simbolos[valor] = len(tabela_simbolos) + 1
                    tokens_encontrados.append((nome, tabela_simbolos[valor]))
                else:
                    # Senão, adiciona o token à lista de tokens encontrados
                    tokens_encontrados.append((nome, valor))
                posicao += len(valor)
                break

        # Se não foi possível casar com nenhum token, registra um erro léxico
        if not match:
            erros.append((expressao[posicao], posicao))
            posicao += 1

    # Retorna a lista de tokens encontrados e a lista de erros
    return tokens_encontrados, erros

# Exemplo de uso
expressao = 'x = 5 - 1.3 * 4 + 1)\n'
tabela_simbolos = {}
tokens_encontrados, erros = analisar(expressao)

# Imprime os tokens encontrados e os erros (se houverem)
print('Tokens encontrados:')
for token in tokens_encontrados:
    print(token)
print('Erros:')
for erro in erros:
    print(erro)