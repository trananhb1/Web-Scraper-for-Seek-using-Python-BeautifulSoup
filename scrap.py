import requests
from bs4 import BeautifulSoup
import pandas as pd
i=1
loop = True
columns =  ['Job Title', 'Job Listed','Company hire','Job Description'] 
jobs= pd.DataFrame({},columns = columns)
while(loop):
    
    url = 'https://www.seek.com.au/python-developer-jobs/in-All-Melbourne-VIC?page=%d' % i

    print('Loading page %d ...' % i )
    i += 1
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elems = soup.find_all('article', class_ = '_2m3Is-x _3KQ6cQG')
    if len(job_elems) == 0:
        print('No more job')
        loop = False
        break
    list_class = ['_2iNL7wI','Eadjc1o','_3AMdmRg','bl7UwXp']
    job_obj = [list(map(lambda x: job_elem.find(class_=x).get_text(), list_class)) for job_elem in job_elems]
    job_objs = pd.DataFrame(job_obj, columns = columns)
    # print(job_objs)
    jobs = jobs.append(job_objs, ignore_index = True)
    # print(jobs)
print(jobs)

