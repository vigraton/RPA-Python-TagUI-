import rpa as r
import pyautogui

print('Iniciando tarefa automatizada...')

r.init()
r.url('https://www.google.com.br/') 
r.wait(1)
r.click('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') # Barra de pesquisa
r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'www8.receita.fazenda.gov.br/SimplesNacional/[enter]')
r.wait(2)
r.click('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a') # Simples nacional 
r.wait(1)
r.hover('//*[@id="botaoSimples"]') 
r.click('//*[@id="menuSimples"]/ul/li[2]/a')
r.wait(1)
r.click('//*[@id="grupo"]/table/tbody/tr[2]/td[3]/a/img') 
r.wait(5)

pyautogui.locateOnScreen('//*[@id="login-dados-certificado"]/p[2]')
r.wait('5')
pyautogui.click('//*[@id="login-dados-certificado"]/p[2]')


