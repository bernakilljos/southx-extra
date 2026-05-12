import requests,os
base='https://moderngov.southwark.gov.uk/'
# fetch weekly meetings plus all linked docs recursively
pages=['ieListDocuments.aspx?CId=172&MId=8402','ieListDocuments.aspx?CId=327&MId=8405','ieListDocuments.aspx?CId=519&MId=8249','ieListDocuments.aspx?CId=650&MId=8178','ieListDocuments.aspx?CId=172&MId=8403','ieListDocuments.aspx?CId=171&MId=8320']
os.makedirs('data',exist_ok=True)
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
for i,p in enumerate(pages):
 r=requests.get(urljoin(base,p));print(i,p,r.status_code,len(r.content),r.url)
 open(f'data/m{i}.html','wb').write(r.content)
 s=BeautifulSoup(r.text,'html.parser')
 # capture PDFs/doc links
 j=0
 for a in s.select('a[href]'):
  href=a['href']; ful=urljoin(r.url,href)
  if not any(x in href.lower() for x in ['.pdf','.doc','mgconvert2pdf','mgconvert2pdf','publicpack.pdf','publicpack agenda']):continue
  try:r2=requests.get(ful,timeout=60);print('  link',j,href[:80],r2.status_code,len(r2.content),r2.url)
  except Exception as e:print('  err',e);continue
  ext='.pdf' if b'%PDF' in r2.content[:20] else '.html'
  open(f'data/m{i}_{j}{ext}','wb').write(r2.content); j+=1
