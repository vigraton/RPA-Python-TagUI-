import rpa as r

print('Testing...')

r.init()

r.url('https://www.google.com')

#LOGADA

r.click('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div')
r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div', 'gmail[enter]') #Buscando gmail
r.click('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3') #OK
r.click('//*[@id="gs_lc50"]/input[1]')
r.type('//*[@id="gs_lc50"]/input[1]', '<E-mail de sua escolha>') #OK
r.click('//*[@id="aso_search_form_anchor"]/button[4]') #OK
r.click('//*[@id=":1"]/div/div[2]/div[5]/div[2]/div[1]/div[1]/span/div') #OK

r.click('//*[@id=":p6"]') #Subjectbox     
r.type('//*[@id=":p6"]', 'Mensagem automatizada') #OK
r.click('//*[@id=":qh"]') #OK
r.type('//*[@id=":qh"]', '<Mensagem de sua escolha>') #OK

r.click('//*[@id=":ow"]')

r.close()






