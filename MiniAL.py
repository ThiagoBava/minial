import re

# Define uma expressão regular para cada tipo de token
regexIdentificador = r'[a-zA-Z]+'
regexNumeroInteiroNegativo = r'-[0-9]+'
regexNumeroInteiroPositivo = r'[0-9]+'
regexNumeroRealNegativo = r'-[0-9]+\.[0-9]+'
regexNumeroRealPositivo = r'[0-9]+\.[0-9]+'
regexSoma = r'\+'
regexSubtracao = r'-'
regexMultiplicacao = r'\*'
regexDivisao = r'/'
regexAtribuicao = r'='
regexParenteses = r'[()]'
regexFimDeLinha = r'\n'

# Associa cada expressão regular a um nome de token
tokens = {
    'NUMERO_REAL_NEGATIVO': regexNumeroRealNegativo,
    'NUMERO_REAL_POSITIVO': regexNumeroRealPositivo,
    'IDENTIFICADOR': regexIdentificador,
    'NUMERO_INTEIRO_NEGATIVO': regexNumeroInteiroNegativo,
    'NUMERO_INTEIRO_POSITIVO': regexNumeroInteiroPositivo,
    'OPERADOR_SOMA': regexSoma,
    'OPERADOR_SUBTRACAO': regexSubtracao,
    'OPERADOR_MULTIPLICACAO': regexMultiplicacao,
    'OPERADOR_DIVISAO': regexDivisao,
    'ATRIBUICAO': regexAtribuicao,
    'ABRE_PARENTESES': regexParenteses,
    'FECHA_PARENTESES': regexParenteses,
    'FIM_DE_LINHA': regexFimDeLinha,
}

# Função para analisar uma expressão
def analisar(expressao):
    # Adiciona um espaço no final da expressão para facilitar a análise
    expressao = expressao.strip() + ' '

    # Inicializa as variáveis de estado
    posicao = 0
    tokensEncontrados = []
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
                    if valor not in tabelaSimbolos:
                        tabelaSimbolos[valor] = len(tabelaSimbolos) + 1
                    tokensEncontrados.append((nome, valor))
                else:
                    # Senão, adiciona o token à lista de tokens encontrados
                    tokensEncontrados.append((nome, valor))
                posicao += len(valor)
                break

        # Se não foi possível casar com nenhum token, registra um erro léxico
        if not match:
            erros.append((expressao[posicao], posicao))
            posicao += 1

    # Retorna a lista de tokens encontrados e a lista de erros
    return tokensEncontrados, erros

# Exemplo de uso
expressao = '-32.3 * X + 7'
# expressao = input("Digite sua expressão: ")
tabelaSimbolos = {}
tokensEncontrados, erros = analisar(expressao)

# Imprime os tokens encontrados e os erros
print('Tokens encontrados:')
for token in tokensEncontrados:
    print(token)
print('Erros:')
for erro in erros:
    print(erro)