import requests,os
base='https://moderngov.southwark.gov.uk/'
o='data/fullitems';os.makedirs(o,exist_ok=True)
s=requests.Session();s.headers['User-Agent']='Mozilla/5.0'
for id in [76150,76151,76152,76153]:
 r=s.get(base+f'mgAi.aspx?ID={id}');print(id,r.status_code,len(r.text));open(f'{o}/{id}.html','wb').write(r.content)
