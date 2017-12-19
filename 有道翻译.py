import urllib.request
import urllib.parse
import json #html是一个json的字符串，需要用此模块编译成字典


content = input('请输入翻译的内容：')
date['type'] = 'AUTO'
date['i'] = content
date['doctype'] = 'json'
date['xmlVersion'] = 'fanyi.web'
date['ue'] = 'UTF-8'
date['typoResult'] = 'true'
date = urllib.parse.urlencode(date).encode('UTF-8') #urlopen里的date需要先这么编码

res = urllib.request.urlopen(url,date)
html = res.read().decode('UTF-8')

tar = json.loads(html)

print('翻译结果时：%s' % (tar['translateResult'][0][0]['tgt']))
