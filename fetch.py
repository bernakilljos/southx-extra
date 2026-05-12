import requests,os
os.makedirs('data/ind',exist_ok=True)
base='https://moderngov.southwark.gov.uk/'
from bs4 import BeautifulSoup
from urllib.parse import urljoin
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)'}
s=requests.Session();s.headers.update(headers)
for i,p in enumerate(['ieListDocuments.aspx?CId=519&MId=8249','ieListDocuments.aspx?CId=171&MId=8320']):
 r=s.get(urljoin(base,p));soup=BeautifulSoup(r.text,'html.parser');open(f'data/new_m{i}.html','wb').write(r.content);print(i,'page',r.status_code,len(r.content))
 for j,a in enumerate(soup.select('a[href*="documents/s"]')):
  u=urljoin(r.url,a['href']);r2=s.get(u,headers={'Referer':r.url,'User-Agent':'Mozilla/5.0'}); print(i,j,r2.status_code,len(r2.content),a['href'][:60]);open(f'data/ind/m{i}_{j}.pdf','wb').write(r2.content)
