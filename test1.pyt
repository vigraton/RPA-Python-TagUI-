import rpa as r

print('Please work ;-;')

r.init()

r.url('https://www.google.com')
r.url('https://www.youtube.com/')

r.click('//*[@id="search-input"]')
r.type('//*[@id="search-input"]', 'mario soundtrack')
r.click('//*[@id="search-icon-legacy"]')
r.click('//*[@id="video-title"]/yt-formatted-string')