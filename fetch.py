import requests,os
base='https://moderngov.southwark.gov.uk/'
s=requests.Session();
r=s.get(base+'ieListDocuments.aspx?CId=519&MId=8249');print('cookie',s.cookies.get_dict())
from urllib.parse import urljoin
u=urljoin(base,'documents/s131118/Local%20Practice%20Menopause%20in%20Southwark.pdf')
for i,kwargs in enumerate([
 {}, {'headers':{'Referer':r.url}}, {'headers':{'Referer':r.url,'User-Agent':'Mozilla/5.0'}}, {'params':{'T':9}}, {'params':{'T':10}}, {'params':{'CT':2}}, {'params':{'T':0,'CT':2,'MID':8249}},
]):
 r2=s.get(u,**kwargs); print(i,r2.url,r2.status_code,len(r2.content),r2.text[:80] if len(r2.content)<300 else '')
 os.makedirs('data',exist_ok=True);open(f'data/try{i}','wb').write(r2.content)
for i,url in enumerate(['mgChooseDocPack.aspx?ID=8249','mgChooseDocPack.aspx?ID=8320']):
 rr=s.get(urljoin(base,url)); print('packpage',i,rr.status_code,len(rr.content),rr.url)
 open(f'data/choose{i}.html','wb').write(rr.content)
