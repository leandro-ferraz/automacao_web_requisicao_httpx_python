import httpx
import urllib3
import re

#Cada sistema web possui uma construção diferente, possuindo também sua própria forma de comunicação com o servidor (requisição)
#Esta classe deve ser modificada para atender o escopo e as particularidades de cada automação
class Requisicao:
    def __init__(self, cookie):
        self.url = 'https:xxxxxxxx.xxxxxx?page='
        self.header = {
            'method':'GET',
            'authority':'xxxxxxxx.xxxxxx',
            'scheme':'https',
            'path':'/work-items?page=',
            'accept-encoding':'gzip, deflate, br',
            'cookie': cookie
        }
        self.data = None

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    def enviarRequisicaoGet(self, numPgAPesquisar = '1'):
        currentUrl = self.url
        currentHeader = self.header

        #Acrescentando o num da pg nos elementos que forem necessários - nesse caso na url e no 'path' do header        
        currentUrl += str(numPgAPesquisar)
        currentHeader['path'] += str(numPgAPesquisar) 

        response = httpx.get(currentUrl, headers=currentHeader, verify=False, timeout=5)
        self.atualizarCookiesAcme(response.headers['set-cookie'])
        return response

    def enviarRequisicaoPost(self):
        response = httpx.post(self.url, headers=self.header, data=self.data, verify=False, timeout=5)
        return response
    
    def atualizarCookiesAcme(self, headerCookieOfResponse):
        regexPattern = r"((.*).*(.*))"
        cookieAcme = re.search(regexPattern, headerCookieOfResponse)
        self.header['cookie'] = cookieAcme if cookieAcme is not None else print('cookie não encontrado na response do request')
    