import requests
base='https://moderngov.southwark.gov.uk/'
paths=['mgCalendarMonthView.aspx?GL=1&bcr=1','mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026','mgCalendarMonthView.aspx?bcr=1&GL=1&NoBdr=1','mgCalendarMonthView.aspx?M=1&Y=2026&GL=1&bcr=1','mgCalendarMonthView.aspx?M=1&Y=2026&bcr=1']
import os;os.makedirs('data',exist_ok=True)
for i,p in enumerate(paths):
 r=requests.get(base+p);open(f'data/cal{i}.html','wb').write(r.content);print(i,r.status_code,len(r.content),r.url)
for i,h in enumerate(['https://southwark.moderngov.co.uk/','http://moderngov.southwark.gov.uk/']):
 r=requests.get(h+'mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026');open(f'data/alt{i}.html','wb').write(r.content);print('alt',i,r.status_code,len(r.content),r.url)
