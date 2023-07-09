# Projeto para automação usando requisição HTTP

## Descrição do projeto
Esse projeto elimina a etapa de visualização e interação com interfaces web ao enviar diretamente uma requisição http para os servidores. Para tal, é necessário entender as requisições trafegadas. 
Esse projeto possui a estrutura para um caso de uso em específico, mas os dados sensíveis foram apagados - servindo apenas como referência.

## Considerações
O projeto foi criado considerando um caso de uso específico, ao analisar as requisições de um site. Para cada site deverão ser feitas as devidas alterações.

## Bibliotecas usadas
- httpx - a principal
- pandas - para visualização de tabelas html da resposta da requisição
- re - regex para extração de dados necessários
- urllib3 - para desativar mensagens de aviso sobre a segurança das requisições

## Documentação das bibliotecas usadas
- httpx: https://www.python-httpx.org/
- pandas: https://pandas.pydata.org/docs/
- re: https://docs.micropython.org/en/latest/library/re.html
- urllib3: https://urllib3.readthedocs.io/en/stable/

## Principais modificações à considerar
1. Necessidade do uso da lógica criada para o número da pagina (numPgAPesquisar)
2. Necessidade do uso do pandas (caso a resposta seja um html contendo uma tabela)
3. Atualizar o self.url, self.header e self.data da classe Requisição
- caso seja uma requisição post (envio de dados para o servidor), o atributo self.data deve ser preenchido
4. Necessidade do uso da lógica do currentUrl e currentHeader no método enviarRequisicaoGet 
5. Atualizar o método atualizarCookies da classe Requisicao para obter o cookie automaticamente
