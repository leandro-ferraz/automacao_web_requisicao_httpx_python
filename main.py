import requisicao
import pandas as pd

if __name__ == '__main__':

    #Não encontrei uma forma de obter o primeiro cookie automaticamente, mas consegui a partir do segundo
    cookie = str(input('Informe o cookie inicial: ')).strip()
    req = requisicao.Requisicao(cookie)
    desejaContinuar = True
    contador = 0

    while desejaContinuar:
        if contador > 0:
            desejaContinuar = str(input('Deseja continuar: ')).strip().lower()
            if desejaContinuar == 'nao':
                break

        numPgAPesquisar = str(input('Informe o número da página a ser pesquisada: ')).strip()
        
        response  = req.enviarRequisicaoGet(numPgAPesquisar)

        #Nesse caso em específico, a resposta da requisição era um HTML contendo também uma tabela
        #O pandas é muito bom para visualizar nesse cenário
        table = pd.read_html(response.text, encoding='utf-8')[0]
        print(table)

        contador+=1

        with open('response.txt', 'wb') as arq:
            arq.write(response.content)